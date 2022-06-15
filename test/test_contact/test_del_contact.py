from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="for delete username", middlename="for delete middlename", ))


    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contact = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contact)
    old_contacts[0:1] = []
    assert old_contacts == new_contact
