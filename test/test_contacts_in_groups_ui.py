import random
from fixture.orm import ORMFixture
from model.group import Group


def test_add_contact_to_group(app, db):
    ormdb = ORMFixture(host=db.host, name=db.name, user=db.user, password=db.password)
    contacts = app.contact.get_contact_list()
    contact = contacts[random.randrange(len(contacts))]
    group = random.choice(db.get_group_list())
    old_contacts_in_group = ormdb.get_contacts_in_group(Group(id=group.id))
    app.contact.add_contact_to_group(contact, group.id)

    new_contacts_in_group = ormdb.get_contacts_in_group(Group(id=group.id))
    assert len(old_contacts_in_group) + 1 == len(new_contacts_in_group) 


def test_delete_contact_from_group(app, db):
    ormdb = ORMFixture(host=db.host, name=db.name, user=db.user, password=db.password)
    groups = db.get_group_list()
    for g in groups:
        contacts_in_group = ormdb.get_contacts_in_group(Group(id=g.id, name=g.name))
        if len(contacts_in_group) > 0 and g.name != "":
            old_contacts_in_group = ormdb.get_contacts_in_group(Group(id=g.id))
            app.contact.delete_contact_from_group(random.choice(contacts_in_group), g.id)
            new_contacts_in_group = ormdb.get_contacts_in_group(Group(id=g.id))
            assert len(old_contacts_in_group) - 1 == len(new_contacts_in_group) 
            break
