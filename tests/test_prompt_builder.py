# tests/test_prompt_builder.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.prompt_builder import build_prompt
def test_build_prompt():
    scenario = "£5.25M Knightsbridge townhouse unsold for 9 months"
    goal = "Secure offer within 60 days"
    constraint = "Do not reduce below £4.2M"
    prompt = build_prompt(scenario, goal, constraint)
    assert scenario in prompt
    assert goal in prompt
    assert constraint in prompt
    assert "diagnosis" in prompt.lower()