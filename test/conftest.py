import i3ipc
from pytest import fixture


@fixture
def i3():
    return i3ipc.Connection()


def clear_workspaces(i3):
    tree = i3.get_tree()
    for workspace in tree.workspaces()[1:]:
        workspace.command('kill')


@fixture
def clean_slate(i3):
    """Kill all workspaces except for workspace 1

    Focused window is moved to workspace 1"""
    tree = i3.get_tree()
    focused = tree.find_focused()
    focused.command("move container to workspace 1")
    clear_workspaces(i3)
    yield i3
    # Tear down any changes to the workspaces from the test function
    clear_workspaces(i3)
    i3.command("workspace 1")
