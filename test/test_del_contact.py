from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="Firstname", lastname="Lastname"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
    # FIXME тест зелёный только в режиме отладки с точками останова
