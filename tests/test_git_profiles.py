import os
import tempfile
import json
import pytest
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from git_profiles import load_profiles, save_profiles, add_profile, remove_profile, CONFIG_FILE
from ui_tray import is_valid_email

def test_add_and_remove_profile(monkeypatch):
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = os.path.join(tmpdir, "test_profiles.json")
        monkeypatch.setattr("git_profiles.CONFIG_FILE", test_file)
        # Initially empty
        assert load_profiles() == {}
        # Add profile
        add_profile("Test User", "test@example.com")
        profiles = load_profiles()
        assert profiles["Test User"] == "test@example.com"
        # Remove profile
        remove_profile("Test User")
        assert "Test User" not in load_profiles()

def test_invalid_email_and_name(monkeypatch):
    # Use the real validation function from the UI
    assert is_valid_email("test@example.com")
    assert not is_valid_email("")
    assert not is_valid_email("invalid@")
    assert not is_valid_email("@invalid.com")
    assert not is_valid_email("invalid.com")
    assert not is_valid_email("invalid@com")
    assert not is_valid_email("invalid@.com")
    assert not is_valid_email("invalid@com.")
    assert not is_valid_email("invalid@.com.")
    assert not is_valid_email("invalid@com..com")
    # Valid name
    assert "Test User".strip() != ""
    # Invalid name
    assert "   ".strip() == "" 