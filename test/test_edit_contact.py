

def test_edit_phone(app):
    app.session.login(username="admin", password="secret")
    app.contact.editFirst(home="48-22-56", mobile="8-800-555-35-35")
    app.session.logout()
