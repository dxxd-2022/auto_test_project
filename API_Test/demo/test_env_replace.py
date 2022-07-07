from auto_test_project.API_Test import env_replace
from auto_test_project.API_Test.env_replace import Env


class TestEnv(Env):
    data = {
        "method": "get",
        "url": "http://testing-studio:9999/base64_demo.txt",
        "headers": None
    }
    def test_env_replace(self):
        req=env_replace.Env()
        print(req.env_replace(self.data).text)

