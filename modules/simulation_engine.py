# modules/simulation_engine.py

from modules.scorer import calculate_simulation_score

def simulate_gpt_response(prompt, scenario=None, goal=None, constraint=None):
    """
    Simulates an LLM response. Returns structured dict as if from GPT.
    Uses the scorer module.
    """
    score = calculate_simulation_score(
        scenario or "", goal or "", constraint or ""
    )
    return {
        "diagnosis": "The current guide price exceeds buyer tolerance based on local liquidity compression.",
        "strategic_actions": [
            "Reposition guide to £4.25M",
            "Switch to performance-led agent within 14 days",
            "Reframe marketing with withdrawn comp narrative"
        ],
        "simulation_score": score
    }