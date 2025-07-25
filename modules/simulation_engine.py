# modules/simulation_engine.py

from modules.context import domain_context
from modules.domain_profiles import DOMAIN_PROFILES
from modules.scorer import calculate_simulation_score

def simulate_gpt_response(prompt, scenario=None, goal=None, constraint=None):
    try:
        from modules.openai_client import query_openai_gpt
        from modules.gpt_parser import parse_gpt_output

        domain = domain_context["active_domain"]
        gpt_output = query_openai_gpt(prompt, domain) 
        print("\n[DEBUG] GPT RAW OUTPUT:\n", gpt_output)

        if gpt_output.strip().startswith("Error:"):
            print("\n[DOMAIN ERROR] GPT refused input:")
            print(gpt_output)
            exit(1)

        parsed = parse_gpt_output(gpt_output)

        # Use domain-specific scoring if available
        profile = DOMAIN_PROFILES.get(domain, {})
        scorer_func = profile.get("scoring_function")
        if scorer_func:
            parsed["simulation_score"] = scorer_func(scenario, goal, constraint)
        else:
            parsed["simulation_score"] = calculate_simulation_score(scenario, goal, constraint)

        required = ["diagnosis", "strategic_actions", "forecast", "commentary", "simulation_score"]
        if not all(parsed.get(key) for key in required):
            raise ValueError("GPT response missing one or more required fields.")

        return parsed

    except Exception as e:
        print("Error: Could not get a valid GPT response.")
        print(e)
        exit(1)