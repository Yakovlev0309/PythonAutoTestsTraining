from model.contact import Contact


def test_modify_contact_phone(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(home="48-22-56", mobile="8-800-555-35-35"))
    app.session.logout()
