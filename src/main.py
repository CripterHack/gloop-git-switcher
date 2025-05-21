import os
import json
import subprocess
import requests
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QInputDialog
from PyQt5.QtGui import QIcon

CONFIG_FILE = os.path.expanduser("~/.git_profiles.json")
ICON_PATH = os.path.expanduser("~/.git_user_icon.png")
DEFAULT_ICON = os.path.join(os.path.dirname(__file__), "../assets/gittrayapp_icon_128x128.png")

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

def get_current_git_user():
    try:
        name = subprocess.check_output(["git", "config", "--global", "user.name"]).decode().strip()
        email = subprocess.check_output(["git", "config", "--global", "user.email"]).decode().strip()
        return name, email
    except subprocess.CalledProcessError:
        return None, None

def set_git_user(name, email):
    subprocess.run(["git", "config", "--global", "user.name", name])
    subprocess.run(["git", "config", "--global", "user.email", email])

def fetch_github_avatar(email):
    try:
        res = requests.get(f"https://api.github.com/search/users?q={email}+in:email")
        if res.status_code == 200:
            users = res.json().get("items", [])
            if users:
                avatar_url = users[0].get("avatar_url")
                img_data = requests.get(avatar_url).content
                with open(ICON_PATH, "wb") as f:
                    f.write(img_data)
                return True
    except Exception:
        pass
    return False

def get_user_icon(email):
    if fetch_github_avatar(email):
        return QIcon(ICON_PATH)
    elif os.path.exists(DEFAULT_ICON):
        return QIcon(DEFAULT_ICON)
    else:
        return QIcon()

class GitTrayApp:
    def __init__(self):
        self.app = QApplication([])
        self.menu = QMenu()
        name, email = get_current_git_user()
        self.tray = QSystemTrayIcon(get_user_icon(email))
        self.tray.setContextMenu(self.menu)
        self.tray.setToolTip("Gloop — Git User Switcher")
        self.update_menu()
        self.tray.show()
        self.app.exec_()

    def update_menu(self):
        self.menu.clear()
        profiles = load_profiles()
        current_name, current_email = get_current_git_user()
        self.tray.setIcon(get_user_icon(current_email))
        self.menu.addAction(f"Actual: {current_name} <{current_email}>")
        self.menu.addSeparator()
        for name, email in profiles.items():
            action = QAction(f"{name} <{email}>")
            action.triggered.connect(lambda _, n=name, e=email: self.switch_user(n, e))
            self.menu.addAction(action)
        self.menu.addSeparator()
        self.menu.addAction("Agregar nuevo perfil", self.add_profile)
        self.menu.addAction("Salir", self.app.quit)

    def switch_user(self, name, email):
        set_git_user(name, email)
        self.update_menu()

    def add_profile(self):
        name, ok1 = QInputDialog.getText(None, "Nuevo perfil", "Nombre:")
        if not ok1 or not name:
            return
        email, ok2 = QInputDialog.getText(None, "Nuevo perfil", "Correo:")
        if not ok2 or not email:
            return
        profiles = load_profiles()
        profiles[name] = email
        save_profiles(profiles)
        self.update_menu()

if __name__ == "__main__":
    ensure_config_file()
    GitTrayApp()
