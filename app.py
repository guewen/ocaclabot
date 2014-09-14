import json
from flask import Flask, request
from pprint import pprint as pp

app = Flask(__name__)


MAX_HISTORY = 50
history = []


def add_to_history(push):
    history = history[:MAX_HISTORY]
    history.append(push)


class GitHubPush(object):

    def __init__(self, data):
        self.data = data

    def repo_name():
        return self.data.get('repository', {}).get('full_name', '')

    def owner_name():
        return self.data.get('repository', {}).get('owner', {}).get('name', '')

    def commits():
        return self.data.get('commits', [])


@app.route('/')
def index():
    template = ('<html><head><title>OCA CLA</title></head>'
                '<body><table>%s</table></body></html>')
    page = template % '\n'.join(['<tr><td>%s</td><td>%s</td></tr>' %
                                 (push.repo_name(),
                                  push.owner_name()) for push in history])
    return page


@app.route('/hook', methods=['POST'])
def hook():
    data = json.loads(request.data)
    event = request.headers['X-GitHub-Event']
    pp(request.headers)
    pp(event)
    pp(data)
    if event == 'push':
        add_to_history(GitHubPush(data))
    return 'OK'
