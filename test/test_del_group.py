

def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.deleteFirstGroup()
    app.session.logout()
