# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.openHomePage()
    app.session.login(username="admin", password="secret")
    app.openGroupsPage()
    app.createGroup(
        Group(name="test group", header="test header", footer="test footer")
    )
    app.returnToGroupsPage()
    app.session.logout()


def test_add_empty_group(app):
    app.openHomePage()
    app.session.login(username="admin", password="secret")
    app.openGroupsPage()
    app.createGroup(Group(name="", header="", footer=""))
    app.returnToGroupsPage()
    app.session.logout()
