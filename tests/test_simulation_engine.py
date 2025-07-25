import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.simulation_engine import simulate_gpt_response
from modules.scorer import calculate_simulation_score

def simulate_gpt_response(prompt, scenario=None, goal=None, constraint=None):
    """
    Tries to get a real GPT response and parse it.
    If not possible, or parsing fails, returns the simulated/dummy response.
    """
    try:
        from modules.openai_client import query_openai_gpt
        from modules.gpt_parser import parse_gpt_output

        gpt_output = query_openai_gpt(prompt)
        print("\n[DEBUG] OpenAI GPT output:", gpt_output)
        parsed = parse_gpt_output(gpt_output)
        # Check for valid output structure (optional)
        if not parsed["diagnosis"] or not parsed["strategic_actions"] or parsed["simulation_score"] is None:
            raise ValueError("GPT response missing expected fields")
        return parsed

    except Exception as e:
        # Fallback to simulation
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