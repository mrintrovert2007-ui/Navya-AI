from agents.desktop_agent import open_notepad, open_calculator


def execute(action):

    if action["action"] == "open_app":

        app = action["app"]

        if app == "notepad":
            open_notepad()
            return "Opening Notepad..."

        elif app == "calculator":
            open_calculator()
            return "Opening Calculator..."

        else:
            return f"I don't know how to open {app}."

    elif action["action"] == "chat":
        return action["message"]

    else:
        return "Unknown action."