# -*- coding: utf-8 -*-
import pytest
from application import Application
from group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.openHomePage()
    app.login(username="admin", password="secret")
    app.openGroupsPage()
    app.createGroup(Group(name="test group", header="test header", footer="test footer"))
    app.returnToGroupsPage()        
    app.logout()
    
        
def test_add_empty_group(app):
    app.openHomePage()
    app.login(username="admin", password="secret")
    app.openGroupsPage()
    app.createGroup(Group(name="", header="", footer=""))
    app.returnToGroupsPage()        
    app.logout()
