import json
from flask import Flask, request
from pprint import pprint as pp

app = Flask(__name__)


MAX_HISTORY = 50
history = []


def add_to_history(push):
    history = history[:MAX_HISTORY]
    history.append(push)


@app.route('/')
def index():
    template = ('<html><head><title>OCA CLA</title></head>'
                '<body><table>%s</table></body></html>')
    page = template % '\n'.join(['<tr><td>%s</td><td>%s</td></tr>' %
                                 (push['ref'], push['after']) for push
                                 in history])
    return page


@app.route('/hook', methods=['POST'])
def hook():
    data = json.loads(request.data)
    event = request.headers['X-GitHub-Event']
    pp(request.headers)
    pp(event)
    pp(data)
    if event == 'push':
        add_to_history(data)
    return 'OK'
