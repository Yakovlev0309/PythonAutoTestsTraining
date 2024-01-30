from model.contact import Contact


def test_modify_contact_phone(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="Firstname", lastname="Lastname"))
    app.contact.modify_first_contact(Contact(home="48-22-56", mobile="8-800-555-35-35"))


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="", lastname="Lastname"))
    app.contact.modify_first_contact(Contact(firstname="Sergey", lastname="Brin", nickname="brin_goog"))
