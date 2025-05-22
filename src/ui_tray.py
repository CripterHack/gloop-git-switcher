from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QInputDialog, QMessageBox
from git_profiles import load_profiles, add_profile, remove_profile, ensure_config_file
from git_user import get_current_git_user, set_git_user
from avatar import get_user_icon
import re

EMAIL_REGEX = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

def is_valid_email(email):
    if not re.match(EMAIL_REGEX, email):
        return False
    if ".." in email:
        return False
    return True

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
        if not current_name or not current_email or current_name == "None" or current_email == "None":
            self.menu.addAction("⚠️ Git is not configured correctly").setEnabled(False)
        else:
            self.menu.addAction(f"Current: {current_name} <{current_email}>").setEnabled(False)
        self.menu.addSeparator()
        if profiles:
            for name, email in profiles.items():
                submenu = QMenu(f"{name} <{email}>")
                switch_action = QAction("Switch to this profile")
                switch_action.triggered.connect(lambda _, n=name, e=email: self.switch_user(n, e))
                submenu.addAction(switch_action)
                delete_action = QAction("Delete this profile")
                delete_action.triggered.connect(lambda _, n=name: self.confirm_delete_profile(n))
                submenu.addAction(delete_action)
                self.menu.addMenu(submenu)
        else:
            self.menu.addAction("No saved profiles").setEnabled(False)
        self.menu.addSeparator()
        self.menu.addAction("Add new profile", self.add_profile)
        self.menu.addAction("Quit", self.app.quit)

    def switch_user(self, name, email):
        try:
            set_git_user(name, email)
            QMessageBox.information(None, "User switched", f"Global Git user changed to:\n{name} <{email}>")
        except Exception as e:
            QMessageBox.critical(None, "Error switching user", str(e))
        self.update_menu()

    def add_profile(self):
        name, ok1 = QInputDialog.getText(None, "New profile", "Name:")
        if not ok1 or not name or not name.strip():
            QMessageBox.warning(None, "Invalid name", "You must enter a valid name.")
            return
        email, ok2 = QInputDialog.getText(None, "New profile", "Email:")
        if not ok2 or not email or not is_valid_email(email):
            QMessageBox.warning(None, "Invalid email", "You must enter a valid email address.")
            return
        add_profile(name.strip(), email.strip())
        QMessageBox.information(None, "Profile added", f"Profile {name} <{email}> added successfully.")
        self.update_menu()

    def confirm_delete_profile(self, name):
        reply = QMessageBox.question(None, "Delete profile", f"Are you sure you want to delete the profile '{name}'?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            remove_profile(name)
            QMessageBox.information(None, "Profile deleted", f"Profile '{name}' deleted.")
            self.update_menu() 