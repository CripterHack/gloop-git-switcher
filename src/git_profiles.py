import os
import json

CONFIG_FILE = os.path.expanduser("~/.git_profiles.json")

def ensure_config_file():
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "w") as f:
            json.dump({}, f)

def load_profiles():
    ensure_config_file()
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_profiles(profiles):
    with open(CONFIG_FILE, "w") as f:
        json.dump(profiles, f, indent=4)

def add_profile(name, email):
    profiles = load_profiles()
    profiles[name] = email
    save_profiles(profiles)

def remove_profile(name):
    profiles = load_profiles()
    if name in profiles:
        del profiles[name]
        save_profiles(profiles) 