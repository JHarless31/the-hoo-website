from flask import Flask, render_template, jsonify

app = Flask(__name__)

ACTIONS = [
  {
    'id': 1,
    'name': 'Move',
    'cost': 1,
    'difficulty': 'Easy'
  },
  {
    'id': 2,
    'name': 'Interact',
    'cost': 2,
    'difficulty': 'Medium'
  },
  {
    'id': 3,
    'name': 'Search',
    'cost': 3,
    'difficulty': 'Medium'
  },
  {
    'id': 4,
    'name': 'Attack',
    'cost': 4,
    'difficulty': 'Hard'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', actions=ACTIONS)

@app.route("/api/actions")
def list_actions():
  return jsonify(ACTIONS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)