from model.contact import Contact

import conftest

def test_modify_first_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="New Test"))
    app.session.logout()

def test_modify_first_contact_middlename(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(middlename="New Test"))
    app.session.logout()