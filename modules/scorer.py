import re

def calculate_simulation_score(scenario, goal, constraint):
    """
    Domain-agnostic scoring logic.
    Produces a simulation score between 0.0 and 0.95 based on:
    - Scenario richness
    - Goal urgency
    - Constraint rigidity
    - Conflict between goal and constraint
    """

    score = 0.5

    # 1. Scenario richness (longer = more realistic / more context)
    score += min(len(scenario.strip()) / 300, 0.15)  # up to +0.15

    # 2. Goal urgency or clarity
    if re.search(r"\b(in|within|under)\s*\d+\s*(days|weeks|hours)", goal.lower()):
        score += 0.05  # urgency
    if any(kw in goal.lower() for kw in ["achieve", "deliver", "secure", "solve", "launch", "complete"]):
        score += 0.05

    # 3. Constraint rigidity
    if re.search(r"\b(do not|must not|cannot|never|strictly)\b", constraint.lower()):
        score -= 0.1
    if re.search(r"\b(must|only|exactly|no deviation|hard limit)\b", constraint.lower()):
        score -= 0.05

    # 4. Conflict signal (goal vs constraint)
    if (
        ("increase" in goal.lower() and "limit" in constraint.lower()) or
        ("reduce" in goal.lower() and "minimum" in constraint.lower()) or
        ("fast" in goal.lower() and "no change" in constraint.lower())
    ):
        score -= 0.1

    return round(max(0.0, min(score, 0.95)), 2)