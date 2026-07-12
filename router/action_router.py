from agents.desktop_agent import open_application
from agents.browser_agent import web_search, open_url
from agents.keyboard_agent import type_text, press_key, hotkey
from agents.mouse_agent import click, move_mouse, scroll
from agents.system_agent import adjust_volume, mute_volume, lock_screen
from agents.window_agent import close_active_window, minimize_window, maximize_window
from agents.vision_agent import click_element_by_vision

def route_action(action_data: dict) -> str:
    """
    Takes the parsed JSON command from the LLM and routes it to the correct OS agent.
    """
    if not isinstance(action_data, dict):
        return "Error: Action data is not a valid dictionary."

    action_type = action_data.get("action", "").lower()
    
    # ---------------------------------------------------------
    # 1. VISION ASSISTANT (New)
    # ---------------------------------------------------------
    if action_type == "vision_click":
        element = action_data.get("element")
        if not element:
            return "Error: No target element specified for vision_click."
        return click_element_by_vision(element)

    # ---------------------------------------------------------
    # 2. DESKTOP & FILES
    # ---------------------------------------------------------
    elif action_type == "open_app":
        app_name = action_data.get("app")
        if not app_name:
            return "Error: No application name provided."
        return open_application(app_name)

    # ---------------------------------------------------------
    # 3. WEB & BROWSER
    # ---------------------------------------------------------
    elif action_type == "web_search":
        query = action_data.get("query")
        return web_search(query)
        
    elif action_type == "open_url":
        url = action_data.get("url")
        return open_url(url)

    # ---------------------------------------------------------
    # 4. KEYBOARD CONTROLS
    # ---------------------------------------------------------
    elif action_type == "type_text":
        text = action_data.get("text")
        return type_text(text)
        
    elif action_type == "press_key":
        key = action_data.get("key")
        return press_key(key)
        
    elif action_type == "hotkey":
        keys = action_data.get("keys", [])
        # Using *keys to unpack the list so it works with your keyboard agent
        return hotkey(*keys) 

    # ---------------------------------------------------------
    # 5. STANDARD MOUSE CONTROLS (Coordinate based)
    # ---------------------------------------------------------
    elif action_type == "click":
        return click()
        
    elif action_type == "move_mouse":
        x = action_data.get("x", 0)
        y = action_data.get("y", 0)
        return move_mouse(x, y)

    # ---------------------------------------------------------
    # 6. SYSTEM CONTROLS
    # ---------------------------------------------------------
    elif action_type == "adjust_volume":
        level = action_data.get("level")
        return adjust_volume(level)
        
    elif action_type == "lock_screen":
        return lock_screen()

    # ---------------------------------------------------------
    # 7. WINDOW MANAGEMENT
    # ---------------------------------------------------------
    elif action_type == "close_window":
        return close_active_window()
        
    elif action_type == "minimize_window":
        return minimize_window()

    # ---------------------------------------------------------
    # 8. CONVERSATIONAL FALLBACK
    # ---------------------------------------------------------
    elif action_type == "chat":
        return action_data.get("message", "I'm not sure what to say.")
        
    elif action_type == "complete":
        return "Task complete."

    # ---------------------------------------------------------
    # UNKNOWN ACTION
    # ---------------------------------------------------------
    else:
        return f"Warning: '{action_type}' is not a recognized action."