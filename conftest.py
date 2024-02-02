import pytest
from fixture.application import Application


fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    if fixture is None: # фикстура не инициализована
        fixture = Application(browser=browser)
    else: # фикстура инициализована
        if not fixture.is_valid(): # фикстура не валидна
            fixture = Application(browser=browser)
    fixture.session.ensure_login(username="admin", password="secret") # обеспечение входа
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
