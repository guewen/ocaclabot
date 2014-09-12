import json
from flask import Flask, request
from prettyprint import prettyprint as pp

app = Flask(__name__)


@app.route('/')
def index():
    return 'Nothing there'


@app.route('/hook', methods=['POST'])
def hook():
    data = json.loads(request.data)
    event = request.headers['X-GitHub-Event']
    pp(event)
    pp(data)
    return 'OK'
