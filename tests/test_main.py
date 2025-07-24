# tests/test_main.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import builtins
import pytest
from main import get_user_input

def test_get_user_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "test")
    result = get_user_input()
    assert result == {
        "scenario": "test",
        "goal": "test",
        "constraint": "test"
    }