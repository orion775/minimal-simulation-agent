# modules/prompt_builder.py


def build_prompt(scenario, goal, constraint):
    """
    Given scenario, goal, and constraint, return a prompt string
    suitable for passing to GPT.
    """
    prompt = (
        f"You are an expert real estate strategist.\n\n"
        f"Scenario: {scenario}\n"
        f"Goal: {goal}\n"
        f"Constraint: {constraint}\n\n"
        f"Give a diagnosis, 2-3 strategic actions, and a probability score for success."
    )
    return prompt