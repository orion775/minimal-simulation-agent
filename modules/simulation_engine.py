# modules/simulation_engine.py

from modules.scorer import calculate_simulation_score

def simulate_gpt_response(prompt, scenario=None, goal=None, constraint=None):
    try:
        from modules.openai_client import query_openai_gpt
        from modules.gpt_parser import parse_gpt_output

        gpt_output = query_openai_gpt(prompt)
        print("\n[DEBUG] GPT RAW OUTPUT:\n", gpt_output)
        parsed = parse_gpt_output(gpt_output)
        required = ["diagnosis", "strategic_actions", "forecast", "commentary", "simulation_score"]
        if not all(parsed.get(key) for key in required):
            raise ValueError("GPT response missing one or more required fields.")
        return parsed

    except Exception as e:
        print("Error: Could not get a valid GPT response.")
        print(e)
        exit(1)