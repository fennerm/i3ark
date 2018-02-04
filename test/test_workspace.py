from i3ark.workspace import *


def test_get_workspace_indices(i3, clean_slate):
    assert get_workspace_indices(i3) == [1]
    i3.command("workspace 2")
    assert get_workspace_indices(i3) == [1, 2]


def test_get_empty_workspace(i3, clean_slate):
    assert get_empty_workspace(i3) == 2
    i3.command("workspace 2")
    i3.command("open")
    assert get_empty_workspace(i3) == 3


def test_get_num_windows(i3, clean_slate):
    assert get_num_windows(i3, 2) == 0
    i3.command("workspace 2")
    i3.command("open")
    assert get_num_windows(i3, 2) == 1
