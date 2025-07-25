import re

def parse_gpt_output(gpt_output):
    """
    Parses GPT output into a dict with diagnosis, strategic actions, forecast, commentary, simulation_score.
    Expects headings exactly as in prompt: Diagnosis:, Strategic Actions:, Forecast:, Commentary:, Simulation Score:
    """
    def extract(label, text, next_labels=None):
        """
        Extracts the text under 'label:' up to the next label in next_labels, or end of text.
        """
        next_labels = next_labels or []
        # Regex: label: <capture until next label or end>
        pattern = fr"{label}:(.*?)(?={'|'.join([re.escape(l+':') for l in next_labels])}|$)"
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        return match.group(1).strip() if match else ""

    diagnosis = extract("Diagnosis", gpt_output, ["Strategic Actions", "Forecast", "Commentary", "Simulation Score"])
    actions_text = extract("Strategic Actions", gpt_output, ["Forecast", "Commentary", "Simulation Score"])
    # Find all lines that start with '-', '*', or number+dot
    actions = re.findall(r"(?:[-*]|\d+\.)\s*(.+)", actions_text)
    forecast = extract("Forecast", gpt_output, ["Commentary", "Simulation Score"])
    commentary = extract("Commentary", gpt_output, ["Simulation Score"])
    # Score (float)
    score_match = re.search(r"Simulation Score:\s*([0-9.]+)", gpt_output, re.IGNORECASE)
    score = float(score_match.group(1)) if score_match else None

    return {
        "diagnosis": diagnosis,
        "strategic_actions": actions,
        "forecast": forecast,
        "commentary": commentary,
        "simulation_score": score
    }
