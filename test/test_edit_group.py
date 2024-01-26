

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.editFirst(header="If you had one shot or one opportunity")
    app.session.logout()
