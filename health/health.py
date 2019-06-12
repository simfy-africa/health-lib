from platform import python_version
import subprocess

from flask import jsonify
from flask.views import MethodView


def git_tag_currently_checked_out():
    checked_out_tag_cmd = 'git name-rev --tags --name-only $(git rev-parse HEAD)'
    # Shell must be True to perform command subsitution
    tag = subprocess.run(checked_out_tag_cmd, shell=True, stdout=subprocess.PIPE)
    tag = tag.stdout.decode('utf-8')
    return tag.strip()  # Comes with a trailing '\n'


class APIHealthResource(MethodView):
    health_data = {
        'api_version': git_tag_currently_checked_out(),
        'python_version': python_version(),
    }

    def get(self):
        return jsonify(self.health_data)
