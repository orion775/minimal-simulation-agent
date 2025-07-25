import re

# modules/gpt_parser.py

import re

def parse_gpt_output(gpt_output):
    """
    Parses GPT output into a dict with diagnosis, strategic actions, forecast, commentary, simulation_score.
    Expects headings exactly as in prompt: Diagnosis:, Strategic Actions:, Forecast:, Commentary:, Simulation Score:
    """
    def extract(label, text, next_labels=None):
        next_labels = next_labels or []
        pattern = fr"{label}:(.*?)(?={'|'.join([re.escape(l+':') for l in next_labels])}|$)"
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        return match.group(1).strip() if match else ""

    diagnosis = extract("Diagnosis", gpt_output, ["Strategic Actions", "Forecast", "Commentary", "Simulation Score"])
    actions_text = extract("Strategic Actions", gpt_output, ["Forecast", "Commentary", "Simulation Score"])
    actions = re.findall(r"(?:[-*]|\d+\.)\s*(.+)", actions_text)
    forecast = extract("Forecast", gpt_output, ["Commentary", "Simulation Score"])
    commentary = extract("Commentary", gpt_output, ["Simulation Score"])
    score_match = re.search(r"Simulation Score:\s*([0-9.]+)", gpt_output, re.IGNORECASE)
    score = float(score_match.group(1)) if score_match else 0.0

    return {
        "diagnosis": diagnosis or "",
        "strategic_actions": actions or [],
        "forecast": forecast or "",
        "commentary": commentary or "",
        "simulation_score": score
    }