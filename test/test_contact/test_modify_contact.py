from model.contact import Contact
import conftest

def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
    app.contact.modify_first_contact(Contact(firstname="New Test"))

def test_modify_first_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(middlename="New Test"))
    app.contact.modify_first_contact(Contact(middlename="New Test"))