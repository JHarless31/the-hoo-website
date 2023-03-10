from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text
app = Flask(__name__)

def load_actions_from_db():
  #use the database engine to open a connection inside the variable "conn" to the database and query the database; save the results in the variable "result"
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM actions"))
  #create a list of dictionaries; each dictionary is a row in the "actions" table
    actions = []
    for row in result.all():
      actions.append(row._asdict())
    return actions

@app.route("/")
def hello_world():
  actions_list = load_actions_from_db()
  return render_template('home.html', actions=actions_list)

@app.route("/api/actions")
def list_actions():
  return jsonify(ACTIONS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)