from model.contact import Contact


def test_modify_contact_phone(app):
    app.contact.modify_first_contact(Contact(home="48-22-56", mobile="8-800-555-35-35"))


def test_modify_contact_name(app):
    app.contact.modify_first_contact(Contact(firstname="Sergey", lastname="Brin", nickname="brin_goog"))
