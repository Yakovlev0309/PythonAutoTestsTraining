from model.contact import Contact, BirthDate
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="Elon", lastname="Musk", nickname="elona51",
                    company="Tesla, SpaceX", address="California, Silicon Valley",
                    homephone="48-22-56", mobilephone="8-800-555-35-35", workphone="666-666", secondaryphone="1-234-567-89-10",
                    birth_date=BirthDate(bday="28", bmonth="June", byear="1971"), notes="Smart person (not an alian)")] + \
                    [Contact(firstname=random_string("", 10), lastname=random_string("", 10))
                     for i in range(4)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
