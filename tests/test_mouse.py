from agents.mouse_agent import *

print("Screen:", pyautogui.size())

print(get_mouse_position())

move_mouse(500, 500)

print(get_mouse_position())

left_click()