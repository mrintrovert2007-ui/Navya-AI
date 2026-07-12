from agents.window_agent import (
    activate_window,
    minimize_window,
    maximize_window,
)

input("Open Notepad and press Enter...")

print(activate_window("notepad"))

input("Press Enter to minimize...")
print(minimize_window("notepad"))

input("Press Enter to maximize...")
print(maximize_window("notepad"))