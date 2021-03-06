# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
        app.session.login("admin", "secret")
        app.group.create(Group(name="fcgdfgdfg", header="sdfsfsdfs", footer="dfgdfgdfgdfg"))
        app.group.vozv_group()
        app.session.logout()


def test_add__empty_group(app):
        app.session.login("admin", "secret")
        app.group.create(Group(name="", header="", footer=""))
        app.group.vozv_group()
        app.session.logout()

