from flask import Flask, render_template, jsonify
from database import load_actions_from_db

app = Flask(__name__)

@app.route("/")
def hello_world():
  actions_list = load_actions_from_db()
  return render_template('home.html', actions=actions_list)

@app.route("/api/actions")
def list_actions():
  return jsonify(ACTIONS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)