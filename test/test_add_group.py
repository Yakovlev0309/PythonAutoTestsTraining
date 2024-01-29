# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="test group", header="test header", footer="test footer"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
