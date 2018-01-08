# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
        app.login("admin", "secret")
        app.sozd_groups(Group(name="fcgdfgdfg", header="sdfsfsdfs", footer="dfgdfgdfgdfg"))
        app.vozv_group()
        app.logout()


def test_add__empty_group(app):
        app.login("admin", "secret")
        app.sozd_groups(Group(name="", header="", footer=""))
        app.vozv_group()
        app.logout()

