from model.group import Group
import conftest
from fixture.group import GroupHelper

def test_modify_group_name(app):
    app.group.modify_first_group(Group(name= "New group"))

def test_modify_group_header(app):
    app.group.modify_first_group(Group(header= "New header"))
