def calculate_simulation_score(scenario, goal, constraint):
    """
    Dummy logic: Returns a float between 0.5 and 0.95
    based on input lengths and keywords.
    (You can make this smarter later.)
    """
    score = 0.7
    if "offer" in goal.lower():
        score += 0.1
    if "constraint" in constraint.lower():
        score -= 0.05
    # Add some variety based on scenario length
    score += min(len(scenario), 50) * 0.001
    return round(min(score, 0.95), 2)