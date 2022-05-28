# -*- coding: utf-8 -*-
from model.group import Group
import conftest

def test_add_group(app):
    app.group.create(Group(name="123", header="123", footer="12345"))


