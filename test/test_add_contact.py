from model.contact import Contact, BirthDate


def test_add_contact(app):
    bdate = BirthDate(bday="28", bmonth="June", byear="1971")
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Elon", lastname="Musk", nickname="elona51", company="Tesla, SpaceX", address="California, Silicon Valley", birth_date=bdate, notes="Smart person (not an alian)")
    app.contact.add(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
