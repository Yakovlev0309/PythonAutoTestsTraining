from model.group import Group
import random


def test_modify_some_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    g = random.choice(old_groups)
    old_groups.remove(g)
    group = g
    group.name = "Modified group"
    # app.group.modify_group_by_index(index, group)
    app.group.modify_group(group)

    new_groups = db.get_group_list()
    old_groups.append(group)
    assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max) # соответствие списков групп из БД и из UI


# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(header="test"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header=""))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)


# def test_modify_group_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group())
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(footer="New footer"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
