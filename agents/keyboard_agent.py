import keyboard
import time


def type_text(text: str):
    keyboard.write(text, delay=0.02)
    return f'Typed: "{text}"'


def press_key(key: str):
    keyboard.press_and_release(key)
    return f"Pressed {key}"


def hotkey(*keys):
    keyboard.press_and_release("+".join(keys))
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