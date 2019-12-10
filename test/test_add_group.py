# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="qwerty", header="qwerty", footer="qwerty")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
