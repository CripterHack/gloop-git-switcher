from git_profiles import ensure_config_file
from ui_tray import GitTrayApp

if __name__ == "__main__":
    ensure_config_file()
    GitTrayApp()
