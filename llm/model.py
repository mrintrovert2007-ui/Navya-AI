from ollama import chat
import json

SYSTEM_PROMPT = """
You are Navya, a highly intelligent desktop automation AI assistant.
You interpret user inputs and map them out into executable system commands.

You must respond exclusively in valid JSON format.

Supported actions format:

1. Open Desktop Applications:
{
    "action": "open_app",
    "app": "app_name"
}

2. Click a dynamic visual element or button on the screen using Vision:
{
    "action": "vision_click",
    "element": "precise description of what to find (e.g., 'the close icon on the top right', 'the profile picture icon', 'the red cancel button')"
}

3. Chat / Final Response:
{
    "action": "chat",
    "message": "Your conversation text here"
}

Rules:
- If a user asks to click on an interface component that cannot be targeted cleanly via terminal scripting or shortcuts, default immediately to the "vision_click" action.
- Describe the 'element' clearly so the background visual subsystem can parse it out from screenshot buffers.
"""

def ask_navya(prompt: str):
    try:
        response = chat(
            model="qwen:8b", # Make sure this matches your installed model
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            format="json"  # <-- FORCES VALID JSON OUTPUT
        )
        
        # Directly parse without string slicing
        return json.loads(response["message"]["content"].strip())

    except json.JSONDecodeError:
        return {"action": "chat", "message": "Sorry, I couldn't understand that."}
    except Exception as e:
        print("Model Error:", e)
        return {"action": "chat", "message": "Something went wrong."}