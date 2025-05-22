import os
import sys
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from avatar import fetch_github_avatar, get_user_icon

class DummyQIcon:
    def __init__(self, path=None):
        self.path = path

def test_fetch_github_avatar(monkeypatch, tmp_path):
    # Mock requests.get
    class DummyResponse:
        def __init__(self, status_code, json_data):
            self.status_code = status_code
            self._json = json_data
        def json(self):
            return self._json
        @property
        def content(self):
            return b"fakeimg"
    def mock_requests_get(url):
        if "api.github.com" in url:
            return DummyResponse(200, {"items": [{"avatar_url": "http://avatar"}]} )
        if "avatar" in url:
            return DummyResponse(200, {})
        raise Exception("Unexpected url")
    monkeypatch.setattr("avatar.requests.get", mock_requests_get)
    # Mock file write
    icon_path = tmp_path / ".git_user_icon.png"
    monkeypatch.setattr("avatar.ICON_PATH", str(icon_path))
    assert fetch_github_avatar("test@example.com")
    assert os.path.exists(icon_path)

def test_fetch_github_avatar_error(monkeypatch):
    def mock_requests_get(url):
        raise Exception("Network error")
    monkeypatch.setattr("avatar.requests.get", mock_requests_get)
    # Should handle the error and return False
    assert not fetch_github_avatar("fail@example.com") 