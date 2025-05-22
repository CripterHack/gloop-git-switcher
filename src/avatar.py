import os
import requests
from PyQt5.QtGui import QIcon

ICON_PATH = os.path.expanduser("~/.git_user_icon.png")
DEFAULT_ICON = os.path.join(os.path.dirname(__file__), "../assets/gloop-icon@128.png")

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