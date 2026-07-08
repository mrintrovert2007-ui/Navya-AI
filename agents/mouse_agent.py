import pyautogui

# Safety settings
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.2


def get_mouse_position():
    x, y = pyautogui.position()

    return {
        "x": x,
        "y": y
    }


def move_mouse(x: int, y: int):

    width, height = pyautogui.size()

    # Prevent invalid coordinates
    if not (0 <= x < width and 0 <= y < height):
        return "Invalid screen coordinates."

    pyautogui.moveTo(x, y, duration=0.3)

    return f"Mouse moved to ({x}, {y})."


def left_click():
    pyautogui.click()
    return "Left click completed."


def right_click():
    pyautogui.rightClick()
    return "Right click completed."


def double_click():
    pyautogui.doubleClick()
    return "Double click completed."


def scroll_up(amount=500):
    pyautogui.scroll(amount)
    return "Scrolled up."


def scroll_down(amount=500):
    pyautogui.scroll(-amount)
    return "Scrolled down."