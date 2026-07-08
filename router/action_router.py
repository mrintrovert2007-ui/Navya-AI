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
from agents.keyboard_agent import (
    type_text,
    press_key,
    hotkey,
    press_enter,
    press_tab,
    press_backspace,
    press_delete,
    press_escape,
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

    # ---------- keyboard ----------
    elif action_type == "type_text":
        return type_text(action["text"])

    elif action_type == "press_key":
        return press_key(action["key"])

    elif action_type == "hotkey":
        return hotkey(*action["keys"])

    elif action_type == "enter":
        return press_enter()

    elif action_type == "tab":
        return press_tab()

    elif action_type == "backspace":
        return press_backspace()

    elif action_type == "delete":
        return press_delete()

    elif action_type == "escape":
        return press_escape()
    return "Unknown action."