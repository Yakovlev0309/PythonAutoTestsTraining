import pytest
from fixture.application import Application


fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None: # фикстура не инициализована
        fixture = Application()
    else: # фикстура инициализована
        if not fixture.is_valid(): # фикстура не валидна
            fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret") # обеспечение входа
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout() # обеспечение выхода
        fixture.destroy() # уничтожение фикстуры
    request.addfinalizer(fin)
    return fixture
