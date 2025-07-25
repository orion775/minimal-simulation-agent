# domain_profiles.py

def real_estate_score(scenario, goal, constraint):
    import re
    score = 0.5

    # 1. Long time on market
    if re.search(r"\b(\d+)\s*(months|month)\b", scenario.lower()):
        months = int(re.search(r"\b(\d+)\s*months?\b", scenario.lower()).group(1))
        if months >= 9:
            score -= 0.05
        if months >= 12:
            score -= 0.1

    # 2. High price sensitivity
    if "penthouse" in scenario.lower() or "townhouse" in scenario.lower():
        score += 0.05  # premium properties => more volatile

    # 3. Urgency in goal
    if re.search(r"\b(in|within|under)\s*\d+\s*(days|weeks)", goal.lower()):
        score += 0.05

    # 4. Constraint rigidity
    if re.search(r"\b(do not|must not|cannot|never|strictly)\b", constraint.lower()):
        score -= 0.05

    # Clamp and round
    return round(max(0.0, min(score, 0.95)), 2)


DOMAIN_PROFILES = {
    "real_estate": {
        "system_prompt": (
            "You are a senior property sales strategist with expertise in luxury real estate markets. "
            "Your job is to analyze underperforming property listings and recommend decisive action.\n\n"
            "If the user's scenario is clearly not related to residential or commercial property sales, "
            "respond with exactly:\n"
            "\"Error: The input is not related to property sales. Please provide a relevant scenario.\""
        ),
        "prompt_template": (
            "A client has submitted the following information:\n\n"
            "Scenario: {scenario}\n"
            "Goal: {goal}\n"
            "Constraint: {constraint}\n\n"
            "As a top-tier strategist, assess this case and return your response with the following clearly labeled sections:\n\n"
            "Diagnosis: <Summarize the core issue based on market, pricing, or agent/seller dynamics>\n"
            "Strategic Actions:\n"
            "- <Concrete recommendation #1>\n"
            "- <Concrete recommendation #2>\n"
            "- <Optional: additional step>\n"
            "Forecast: <Brief probability of success if actions are taken — and why>\n"
            "Commentary: <Any relevant behavioral advice for seller or agent>\n"
            "Simulation Score: <Realistic float between 0.0 and 1.0 to express confidence>\n"
        ),
        "required_sections": [
            "Diagnosis", "Strategic Actions", "Forecast", "Commentary", "Simulation Score"
        ],
        "scoring_function": real_estate_score
    },
    "science": {
        "system_prompt": (
        "You are a senior research advisor with deep expertise in scientific reasoning, experimental methodology, and academic planning.\n\n"
        "IMPORTANT: You are ONLY allowed to respond to inputs related to science, research, or experimentation.\n"
        "If the input appears to be about business, property, finance, sales, or anything NON-SCIENTIFIC, do NOT process it.\n\n"
        "Instead, respond with exactly:\n"
        "\"Error: The input is not related to scientific research. Please provide a relevant scenario.\"\n\n"
        "This rule is absolute. Never engage with non-scientific input."
    ),
        "prompt_template": (
            "A research team has submitted the following case:\n\n"
            "Scenario: {scenario}\n"
            "Goal: {goal}\n"
            "Constraint: {constraint}\n\n"
            "As an expert advisor, assess this plan and return your response in the following structured format:\n\n"
            "Diagnosis: <Summarize the scientific flaw, risk, or uncertainty in the current plan>\n"
            "Strategic Actions:\n"
            "- <Action #1: specific scientific adjustment or validation>\n"
            "- <Action #2: optional experimental recommendation>\n"
            "- <Action #3: any cross-disciplinary opportunity>\n"
            "Forecast: <Estimated likelihood of achieving goal — and under what conditions>\n"
            "Commentary: <Research team behavior, mindset, or process feedback>\n"
            "Simulation Score: <Confidence score from 0.0 to 1.0>"
        ),
        "required_sections": [
            "Diagnosis", "Strategic Actions", "Forecast", "Commentary", "Simulation Score"
        ],
        # No scoring_function → uses fallback!
    }
}

