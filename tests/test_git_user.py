import subprocess
import pytest
from git_user import get_current_git_user, set_git_user

def test_get_current_git_user(monkeypatch):
    def mock_check_output(cmd):
        if "user.name" in cmd:
            return b"Test User"
        if "user.email" in cmd:
            return b"test@example.com"
        raise subprocess.CalledProcessError(1, cmd)
    monkeypatch.setattr(subprocess, "check_output", mock_check_output)
    name, email = get_current_git_user()
    assert name == "Test User"
    assert email == "test@example.com"

def test_set_git_user(monkeypatch):
    called = []
    def mock_run(cmd):
        called.append(cmd)
    monkeypatch.setattr(subprocess, "run", mock_run)
    set_git_user("Test User", "test@example.com")
    assert [
        ["git", "config", "--global", "user.name", "Test User"],
        ["git", "config", "--global", "user.email", "test@example.com"]
    ] == called 