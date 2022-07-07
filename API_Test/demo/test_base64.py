from auto_test_project.API_Test.base64demo import Base64Demo


class TestBase64(Base64Demo):
    data = {
        "method": "get",
        "url": "http://127.0.0.1:9999/base64_demo.txt",
        "headers": None,
        "encoding": "base64"
    }
    def test_base64(self):
        req=Base64Demo()
        print(req.send(self.data))
