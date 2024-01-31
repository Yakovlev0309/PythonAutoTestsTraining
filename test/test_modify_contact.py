from model.contact import Contact


def test_modify_contact_phone(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="Firstname", lastname="Lastname"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(home="48-22-56", mobile="8-800-555-35-35")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0].id = contact.id
    old_contacts[0].home = contact.home
    old_contacts[0].mobile = contact.mobile
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="", lastname="Lastname"))
    app.contact.modify_first_contact(Contact(firstname="Sergey", lastname="Brin", nickname="brin_goog"))
