import json
from flask import Flask, request
from pprint import pprint as pp

app = Flask(__name__)


@app.route('/')
def index():
    return 'Nothing there'


@app.route('/hook', methods=['POST'])
def hook():
    data = json.loads(request.data)
    event = request.headers['X-GitHub-Event']
    pp(request.headers)
    pp(event)
    pp(data)
    return 'OK'
