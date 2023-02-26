from flask import Flask, request, Response, make_response, jsonify
import json

app = Flask(__name__)

state = {
    'enabled': False
}


@app.route('/state/set', methods=['POST'])
def state_set():
    global state
    state = request.json
    return jsonify(state)


@app.route('/state/get')
def state_get():
    return json.dumps(state)


if __name__ == '__main__':
    app.run(debug=True)
