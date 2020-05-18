from platform import python_version

from flask import jsonify
from flask.views import MethodView


class APIHealthResource(MethodView):
    def __init__(self):
        self.health_data = {
            'python_version': python_version(),
        }

    def get(self):
        return jsonify(self.health_data)
