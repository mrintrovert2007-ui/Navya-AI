from agents.desktop_agent import open_application
from agents.browser_agent import open_website, google_search


def execute(action):

    if action["action"] == "open_app":
        return open_application(action["app"])

    elif action["action"] == "open_website":
        return open_website(action["website"])

    elif action["action"] == "search_google":
        return google_search(action["query"])

    elif action["action"] == "chat":
        return action["message"]

    return "Unknown action."