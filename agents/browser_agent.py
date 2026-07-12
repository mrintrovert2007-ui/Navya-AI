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

def search_web(query):
    import webbrowser
    print(f"Searching the web for: {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")
    return f"Searched for {query}"

def web_search(query: str) -> str:
    """Searches the web using the default browser."""
    if not query:
        return "Error: No search query provided."
    encoded_query = urllib.parse.quote(query)
    url = f"https://www.google.com/search?q={encoded_query}"
    webbrowser.open(url)
    return f"Searching Google for: '{query}'"

def open_url(url: str) -> str:
    """Opens a specific URL directly."""
    if not url:
        return "Error: No URL provided."
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    webbrowser.open(url)
    return f"Opening URL: {url}"