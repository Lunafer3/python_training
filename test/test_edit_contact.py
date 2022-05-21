from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(name="th", middlename="hs", lastname="sfgdh", homephone="453", homephone2="33",
                mobile="4", workphone="3", faxphone="333",
                mail="125", mail2="578", mail3="457"))
    app.session.logout()