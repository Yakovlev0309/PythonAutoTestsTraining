from model.group import Group
from model.contact import Contact


def test_group_list(app, db): # app - доступ к пользовательскому интерфейсу, db - доступ к базе данных
    ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contact_list(app, db):
    ui_list = app.contact.get_contact_list()
    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname, lastname=contact.lastname, address=contact.address, 
                       all_emails_from_home_page=contact.all_emails_from_home_page, all_phones_from_home_page=contact.all_phones_from_home_page)
    db_list = map(clean, db.get_contact_list())
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)
