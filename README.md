# Gloop

<p align="center">
  <img src="gloop-icon@512.png" alt="Gloop Logo" width="512" height="512"/>
</p>

Gloop is a cross-platform desktop application that allows you to easily switch between multiple global Git identities (name and email) from the system tray. Designed for developers who manage personal, work, and open source project accounts separately.

---

## ✨ Features

- Detects the current global Git user (`user.name` and `user.email`)
- Switches between different profiles from a system tray menu
- Dynamic icon based on the active user's GitHub avatar
- Stores profiles locally in `~/.git_profiles.json`
- Simple interface and no telemetry

---

## 🚀 Installation

### Requirements

- Python 3.10 or higher
- `git` installed
- Internet connection (optional, to download avatars)

### Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running

```bash
python src/main.py
```

---

## 🧱 Project Structure

```
gloop/
├── assets/                 # Project icons and graphics
├── src/                    # Main source code
│   ├── main.py             # Entry point
│   ├── ui_tray.py          # System tray logic (UI)
│   ├── git_profiles.py     # Git profile management
│   ├── git_user.py         # Git global interaction
│   └── avatar.py           # User avatar fetching
├── tests/                  # Automated tests (pytest)
├── .github/                # GitHub workflows and funding
├── docs/                   # Additional documents
├── requirements.txt
├── pyproject.toml
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── .gitignore
```

---

## 🖼️ Available Icons

* PNG: 16x16, 32x32, 64x64, 128x128, 256x256
* Windows: `gittrayapp_icon.ico`
* macOS: `gittrayapp_icon.icns`

Place these icons in the `assets/` folder.

---

## 🖼️ Visual Usage Example

Below are screenshots of the system tray and the user selection menu in Gloop:

| System Tray (active icon) | User Selection Menu |
|:------------------------:|:------------------:|
| ![Tray Icon](docs/captura_tray.png) | ![User Menu](docs/captura_menu.png) |

**Basic flow:**
1. Click the Gloop icon in the system tray.
2. View the current global Git user and available profiles.
3. Select a profile to instantly change the global Git user (you'll receive visual confirmation).
4. Add new profiles from the menu (name and email are validated).
5. Delete profiles from each profile's context menu (with confirmation).
6. If Git is not configured or there are errors, clear warnings will be shown.

> Gloop validates entered data and provides visual feedback for all important actions, improving experience and robustness.

---

## 🖥️ Building with PyInstaller

### Windows

```bash
pyinstaller --noconfirm --onefile --windowed src/main.py --icon=assets/gittrayapp_icon.ico --name gloop
```

### macOS

```bash
pyinstaller --noconfirm --onefile --windowed src/main.py --icon=assets/gittrayapp_icon.icns --name gloop
```

---

## 🐧 Linux Integration (.desktop)

Create a file `~/.local/share/applications/gloop.desktop` with the following content:

```desktop
[Desktop Entry]
Type=Application
Name=Gloop
Comment=Switch between global Git identities easily
Exec=python3 /path/to/gloop/src/main.py
Icon=/path/to/gloop/assets/gloop-icon@128.png
Terminal=false
Categories=Development;Utility;
StartupNotify=true
```

Make it executable:

```bash
chmod +x ~/.local/share/applications/gloop.desktop
```

---

## 🧪 Automated Tests

Unit tests are located in the `tests/` folder and cover profile management, Git interaction, and avatar fetching. Run all tests with:

```bash
pytest
```

---

## ✅ Future Features Checklist

* [ ] Show tooltip or quick copy of `git clone` with the active user
* [ ] Detect Git provider (GitHub, GitLab) and suggest commands
* [ ] Local configuration per folder (repo-specific mode)
* [ ] Integration with SSH keys and `.ssh/config`
* [ ] User change and activity history
* [ ] Full interface for profile management
* [ ] Multilanguage translation

---

## 🟢 Current Development Status

- MVP 0: ✅ Completed (bootstrap, structure, CI, basic documentation)
- MVP 1: ✅ Completed (core functionality, data validation, visual feedback, automated tests, profile deletion option, robustness validated by tests)
- MVP 2: ⬜ In progress (UX improvements, multiplatform support, advanced error messages)

> All MVP 1 features have been implemented and automatically validated by unit tests. The data validation and visual feedback system meets the robustness and user experience standards defined in the strategic guide.

---

## ❤️ Contributions

See [CONTRIBUTING.md](CONTRIBUTING.md) to learn how you can help with improvements, reports, or translations.

Also see our [Code of Conduct](CODE_OF_CONDUCT.md) to maintain a healthy and respectful environment.

---

## 💸 Support this project

This project is free and has no trackers. If you find it useful, you can support it:

* [GitHub Sponsors](https://github.com/sponsors/cripterhack)

(See `.github/FUNDING.yml`)

---

## 🧠 License

MIT — You can use, modify, and share this project freely.
