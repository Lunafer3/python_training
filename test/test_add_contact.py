# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(
        Contact(name="имя", middlename="отчество", lastname="фамилия", homephone="111111", homephone2="999999",
                mobile="88005553535", workphone="222222", faxphone="333333",
                mail="intec@io.mail", mail2="intes@ru.sand", mail3="inter@gov.gav"))
    app.session.logout()
