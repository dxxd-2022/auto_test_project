
import pytest


@pytest.fixture(params=['tom','curry'],ids=["汤姆","库里"])
def login(request):
    login_name=request.param
    print(f"登陆用户名:{login_name}")
    yield login_name
    print("登录完成")
def test_login(login):
    print(login)