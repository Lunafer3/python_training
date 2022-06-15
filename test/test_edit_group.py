from random import randrange

from model.group import Group


def test_edit_group_by_index(app):
    if app.group.count() == 0:
        app.group.create(Group(gr_name="for edit group"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(gr_name="edit_test111111")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
