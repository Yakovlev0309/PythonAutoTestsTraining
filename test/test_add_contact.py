from model.contact import Contact, BirthDate


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    bdate = BirthDate(bday="28", bmonth="June", byear="1971")
    contact = Contact(firstname="Elon", lastname="Musk", nickname="elona51", company="Tesla, SpaceX", address="California, Silicon Valley", birth_date=bdate, notes="Smart person (not an alian)")
    app.contact.add(contact)
    app.session.logout()
