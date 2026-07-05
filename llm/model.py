from ollama import chat
import json

SYSTEM_PROMPT = """
You are Navya AI.

Convert the user's command into JSON.

Return ONLY valid JSON.

Supported actions:

1. Open desktop application
{
    "action": "open_app",
    "app": "application_name"
}

2. Open website
{
    "action": "open_website",
    "website": "website_name"
}

3. Search Google
{
    "action": "search_google",
    "query": "search text"
}

4. Normal conversation
{
    "action": "chat",
    "message": "reply"
}
"""


def ask_navya(prompt: str):
    try:
        response = chat(
            model="qwen3:8b",
            think=False,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        content = response["message"]["content"].strip()

        start = content.find("{")
        end = content.rfind("}") + 1

        if start == -1 or end == 0:
            return {
                "action": "chat",
                "message": "Sorry, I couldn't understand that."
            }

        json_text = content[start:end]

        return json.loads(json_text)

    except json.JSONDecodeError:
        return {
            "action": "chat",
            "message": "Sorry, I couldn't understand that."
        }

    except Exception as e:
        print("Model Error:", e)

        return {
            "action": "chat",
            "message": "Something went wrong."
        }