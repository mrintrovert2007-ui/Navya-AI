import json
import os
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPS_FILE = os.path.join(BASE_DIR, "data", "apps.json")

# Load configuration into memory ONCE during startup
try:
    with open(APPS_FILE, "r") as file:
        APPS = json.load(file)
except FileNotFoundError:
    APPS = {}
    print(f"Warning: {APPS_FILE} not found.")

def open_application(app_name):
    app_name = app_name.lower()

    if app_name in APPS:
        subprocess.Popen(APPS[app_name])
        return f"Opening {app_name}..."

    return f"{app_name} is not available."