import pytest
from fixture.application import Application
import json


fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        with open(request.config.getoption("--target")) as config_file:
            target = json.load(config_file)
    if fixture is None or not fixture.is_valid(): # фикстура не инициализована или инициализована но не валидна
        fixture = Application(browser=browser, base_url=target["baseUrl"])
    fixture.session.ensure_login(username=target["username"], password=target["password"]) # обеспечение входа
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    global fixture
    def fin():
        if fixture is not None:
            fixture.session.ensure_logout() # обеспечение выхода
            fixture.destroy() # уничтожение фикстуры
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
