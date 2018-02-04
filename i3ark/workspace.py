"""Functions for examining and modifying the i3 workspace"""


def get_empty_workspace(i3):
    """Get the index of the first empty workspace"""
    full_workspaces = get_workspace_indices(i3)
    i = 1
    while i in full_workspaces:
        i = i + 1
    return i


def get_workspace_indices(i3):
    """Get list of current workspace indices"""
    workspaces = i3.get_tree().workspaces()
    indices = [workspace.num for workspace in workspaces]
    return indices


def get_num_windows(i3, workspace_index):
    """Get the number of windows in an i3 workspace"""
    tree = i3.get_tree()
    try:
        windows = tree.workspaces()[workspace_index - 1].leaves()
        num_windows = len(windows)
    except IndexError:
        # Thrown if the workspace is empty
        num_windows = 0

    return num_windows
