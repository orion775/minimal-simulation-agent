import pytest
import sys
import os
from modules.openai_client import query_openai_gpt
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def test_query_openai_gpt_no_key(monkeypatch):
    # Ensure the OPENAI_API_KEY env var is not set
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    with pytest.raises(RuntimeError):
        query_openai_gpt("diagnose this property scenario")