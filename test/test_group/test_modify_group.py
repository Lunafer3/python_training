from model.group import Group
import conftest
from fixture.group import GroupHelper

def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name= "New group"))
    app.session.logout()

def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(header= "New header"))
    app.session.logout()