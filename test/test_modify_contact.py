from model.contact import Contact
import random


def test_modify_some_contact_phone(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(firstname="Firstname", lastname="Lastname"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    old_contacts.remove(contact)
    contact.homephone = "48-22-56"
    contact.mobilephone = "8-800-555-35-35"
    app.contact.modify_contact(contact)

    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max) # соответствие списков групп из БД и из UI


# def test_modify_contact_name(app):
#     if app.contact.count() == 0:
#         app.contact.add(Contact(firstname="", lastname="Lastname"))
#     app.contact.modify_first_contact(Contact(firstname="Sergey", lastname="Brin", nickname="brin_goog"))
