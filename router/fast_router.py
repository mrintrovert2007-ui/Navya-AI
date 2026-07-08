def fast_route(command: str):
    command = command.lower().strip()

    # ---------------- Websites ---------------- #

    websites = {
        "youtube",
        "google",
        "gmail",
        "github",
        "linkedin",
        "instagram",
        "facebook",
        "twitter",
        "x",
    }

    if command.startswith("open "):
        website = command.replace("open ", "").strip()

        if website in websites:
            return {
                "action": "open_website",
                "website": website
            }

    # ---------------- Applications ---------------- #

    apps = {
        "notepad",
        "calculator",
        "paint",
        "cmd",
        "terminal",
        "chrome",
        "edge",
        "vscode",
    }

    if command.startswith("open "):
        app = command.replace("open ", "").strip()

        if app in apps:
            return {
                "action": "open_app",
                "app": app
            }

    # ---------------- Google Search ---------------- #

    if command.startswith("search "):
        return {
            "action": "search_google",
            "query": command.replace("search ", "", 1).strip()
        }

    # ---------------- Mouse ---------------- #

    if command == "left click":
        return {
            "action": "left_click"
        }

    if command == "right click":
        return {
            "action": "right_click"
        }

    if command == "double click":
        return {
            "action": "double_click"
        }

    if command == "scroll up":
        return {
            "action": "scroll_up"
        }

    if command == "scroll down":
        return {
            "action": "scroll_down"
        }

    if command in ["mouse position", "get mouse position"]:
        return {
            "action": "mouse_position"
        }

    # ---------------- No Match ---------------- #

    return None