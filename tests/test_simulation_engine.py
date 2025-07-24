import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.simulation_engine import simulate_gpt_response

def test_simulate_gpt_response():
    prompt = "Pretend this is a GPT prompt"
    scenario = "Luxury home unsold for 12 months"
    goal = "Secure offer"
    constraint = "Do not reduce"
    response = simulate_gpt_response(prompt, scenario, goal, constraint)
    assert isinstance(response, dict)
    assert "diagnosis" in response
    assert "strategic_actions" in response
    assert "simulation_score" in response
    assert isinstance(response["strategic_actions"], list)
    assert isinstance(response["simulation_score"], float)
    # Check that the score is in the valid range
    assert 0.5 <= response["simulation_score"] <= 0.95