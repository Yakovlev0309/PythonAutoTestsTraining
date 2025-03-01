

def test_names_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname


def test_names_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.all_names_from_view_page == merge_names_like_on_view_page(contact_from_edit_page)


def merge_names_like_on_view_page(contact):
    return " ".join(filter(lambda x: x is not None and x != "", 
                           [contact.firstname, contact.middlename, contact.lastname]))
