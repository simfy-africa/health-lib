from unittest.mock import Mock, patch

from flask import Flask

from health import APIHealthResource


class TestAPIHealthResource:

    def setup_method(self):
        app = Flask(__name__)

        class RandomAPIHealthResource(APIHealthResource):
            pass
        app.add_url_rule('/health', view_func=RandomAPIHealthResource.as_view('api_health'))
        self.client = app.test_client()

    @patch('health.health.subprocess.run')
    def test_returns_system_version_if_git_tagged(self, mock_run):
        mock_stdout = Mock()
        mock_run.return_value = mock_stdout
        mock_stdout.stdout = b'v1.1\n'

        response = self.client.get('/health')

        assert response.status_code == 200
        assert response.json['api_version'] == 'v1.1'

    def test_returns_undefined_for_system_version_if_not_git_tagged(self):
        response = self.client.get('/health')

        assert response.status_code == 200
        assert response.json['api_version'] == 'undefined'

    def test_returns_python_version(self):
        response = self.client.get('/health')

        assert response.status_code == 200
        assert response.json['python_version'][0:3] == '3.7'
