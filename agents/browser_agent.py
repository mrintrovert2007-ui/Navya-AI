import webbrowser
from urllib.parse import quote


def open_website(site):
    site = site.lower().strip()

    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "github": "https://github.com",
        "chatgpt": "https://chat.openai.com",
        "gmail": "https://mail.google.com",
        "linkedin": "https://www.linkedin.com",
        "instagram": "https://www.instagram.com",
        "facebook": "https://www.facebook.com",
        "twitter": "https://x.com",
        "spotify": "https://open.spotify.com"
    }

    if site in websites:
        webbrowser.open(websites[site])
        return f"Opening {site}..."

    return f"I don't know the website '{site}'."


def google_search(query):
    query = quote(query)
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return f"Searching Google for '{query}'..."