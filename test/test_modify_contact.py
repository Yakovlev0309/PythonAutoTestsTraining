from model.contact import Contact
from random import randrange


def test_modify_some_contact_phone(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="Firstname", lastname="Lastname"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(homephone="48-22-56", mobilephone="8-800-555-35-35")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index].id = contact.id
    old_contacts[index].home = contact.homephone
    old_contacts[index].mobile = contact.mobilephone
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_modify_contact_name(app):
#     if app.contact.count() == 0:
#         app.contact.add(Contact(firstname="", lastname="Lastname"))
#     app.contact.modify_first_contact(Contact(firstname="Sergey", lastname="Brin", nickname="brin_goog"))
