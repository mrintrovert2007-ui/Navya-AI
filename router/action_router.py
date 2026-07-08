from agents.desktop_agent import open_application
from agents.browser_agent import open_website, google_search
from agents.mouse_agent import (
    move_mouse,
    left_click,
    right_click,
    double_click,
    scroll_up,
    scroll_down,
    get_mouse_position,
)


def execute(action):

    action_type = action.get("action")

    # ---------- Desktop ----------

    if action_type == "open_app":
        return open_application(action["app"])

    # ---------- Browser ----------

    elif action_type == "open_website":
        return open_website(action["website"])

    elif action_type == "search_google":
        return google_search(action["query"])

    # ---------- Mouse ----------

    elif action_type == "mouse_move":
        return move_mouse(action["x"], action["y"])

    elif action_type == "left_click":
        return left_click()

    elif action_type == "right_click":
        return right_click()

    elif action_type == "double_click":
        return double_click()

    elif action_type == "scroll_up":
        return scroll_up()

    elif action_type == "scroll_down":
        return scroll_down()

    elif action_type == "mouse_position":
        return get_mouse_position()

    # ---------- Chat ----------

    elif action_type == "chat":
        return action["message"]

    # ---------- Unknown ----------

    return "Unknown action."