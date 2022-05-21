# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application
from conftest import app

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="123", header="123", footer="12345"))
    app.session.logout()

