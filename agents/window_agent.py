import pygetwindow as gw


def list_windows():
    """
    Return titles of all visible windows.
    """
    titles = []

    for window in gw.getAllWindows():
        title = window.title.strip()

        if title:
            titles.append(title)

    return titles


def find_window(title: str):
    """
    Find a window using partial, case-insensitive matching.
    """

    title = title.lower()

    for window in gw.getAllWindows():

        if title in window.title.lower():

            return window

    return None


def activate_window(title: str):
    """
    Bring a window to the foreground.
    """
    window = find_window(title)

    if window is None:
        return f"Window '{title}' not found."

    try:
        window.activate()
        return f"Activated '{window.title}'"
    except Exception as e:
        return str(e)


def minimize_window(title: str):
    window = find_window(title)

    if window is None:
        return f"Window '{title}' not found."

    window.minimize()

    return f"Minimized '{window.title}'"


def maximize_window(title: str):
    window = find_window(title)

    if window is None:
        return f"Window '{title}' not found."

    window.maximize()

    return f"Maximized '{window.title}'"


def close_window(title: str):
    window = find_window(title)

    if window is None:
        return f"Window '{title}' not found."

    window.close()

    return f"Closed '{window.title}'"