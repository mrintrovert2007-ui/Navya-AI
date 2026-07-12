# agents/keyboard_agent.py
import keyboard
import time

def type_text(text: str):
    if not text:
        return "Error: No text provided to type."
    keyboard.write(text, delay=0.02)
    return f'Typed: "{text}"'

def press_key(key: str):
    if not key:
        return "Error: No key provided."
    keyboard.press_and_release(key)
    return f"Pressed {key}"

def hotkey(*keys):
    if not keys:
        return "Error: No hotkey combination provided."
    # Join keys with '+' (e.g., ['ctrl', 'c'] becomes 'ctrl+c')
    combination = "+".join(keys)
    keyboard.press_and_release(combination)
    return f"Pressed {' + '.join(keys)}"

def press_enter():
    keyboard.press_and_release("enter")
    return "Pressed Enter"

def press_tab():
    keyboard.press_and_release("tab")
    return "Pressed Tab"

def press_backspace():
    keyboard.press_and_release("backspace")
    return "Pressed Backspace"

def press_delete():
    keyboard.press_and_release("delete")
    return "Pressed Delete"

def press_escape():
    keyboard.press_and_release("esc")
    return "Pressed Escape"