import pyautogui
import ollama
import re
import os

def find_button_coordinates(button_name: str) -> tuple:
    """
    Takes a screenshot and asks a local vision model for the 
    [X, Y] coordinates of a specific button.
    """
    image_path = "current_screen.png"
    
    # 1. Capture the screen
    pyautogui.screenshot(image_path)
    
    # 2. Strict prompt forcing coordinate-only output
    prompt = f"""
    Look at this screenshot of my desktop.
    Find the exact center of the '{button_name}'.
    Return ONLY its X and Y pixel coordinates in this exact format: [X, Y].
    Do not explain or add any other text.
    """
    
    try:
        # 3. Call the local vision model
        response = ollama.chat(
            model="llava", # Note: You must run `ollama run llava` in your terminal first
            messages=[{
                "role": "user",
                "content": prompt,
                "images": [image_path]
            }]
        )
        
        output = response["message"]["content"]
        
        # 4. Clean up the screenshot
        if os.path.exists(image_path):
            os.remove(image_path)
            
        # 5. Extract coordinates using Regex
        match = re.search(r'\[(\d+),\s*(\d+)\]', output)
        if match:
            x = int(match.group(1))
            y = int(match.group(2))
            return (x, y)
        else:
            print(f"Failed to parse coordinates from model output: {output}")
            return None
            
    except Exception as e:
        print(f"Vision model error: {e}")
        return None