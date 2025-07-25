# modules/prompt_builder.py


def build_prompt(scenario, goal, constraint):
    """
    Build a prompt for GPT that asks for all required sections in clear, labeled format.
    """
    prompt = (
        f"You are an expert real estate sales strategist.\n\n"
        f"Scenario: {scenario}\n"
        f"Goal: {goal}\n"
        f"Constraint: {constraint}\n\n"
        "Please provide a clear, structured response using these exact section headings and formats:\n"
        "Diagnosis: <explain what's really going wrong>\n"
        "Strategic Actions:\n"
        "- <action 1>\n"
        "- <action 2>\n"
        "Forecast: <probability of offer success and why>\n"
        "Commentary: <agent/seller behaviour to consider>\n"
        "Simulation Score: <number between 0 and 1>\n"
    )
    return prompt