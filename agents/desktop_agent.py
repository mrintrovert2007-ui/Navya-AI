import json
import os
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPS_FILE = os.path.join(BASE_DIR, "data", "apps.json")


def open_application(app_name):
    with open(APPS_FILE, "r") as file:
        apps = json.load(file)

    app_name = app_name.lower()

    if app_name in apps:
        subprocess.Popen(apps[app_name])
        return f"Opening {app_name}..."

    return f"{app_name} is not available."