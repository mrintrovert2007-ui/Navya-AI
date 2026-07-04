from ollama import chat
import json

SYSTEM_PROMPT = """
You are Navya AI.

Your job is to convert the user's request into JSON.

Rules:

If the user wants to open an application:

{
    "action":"open_app",
    "app":"application_name"
}

Examples:

User: Open Notepad

{
    "action":"open_app",
    "app":"notepad"
}

User: Open Calculator

{
    "action":"open_app",
    "app":"calculator"
}

If it is normal conversation:

{
    "action":"chat",
    "message":"your answer"
}

Return ONLY JSON.
"""

def ask_navya(prompt):

    response = chat(
        model="qwen3:8b",
        messages=[
            {
                "role":"system",
                "content":SYSTEM_PROMPT
            },
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return json.loads(response["message"]["content"])