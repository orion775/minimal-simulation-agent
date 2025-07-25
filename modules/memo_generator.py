def export_simulation_memo(sim_output, scenario_text=None, filename="simulation_memo.md"):
    """
    Creates a 1-page natural-language summary memo.
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write("# Simulation Memo\n\n")

        if scenario_text:
            f.write(f"**Scenario:** {scenario_text}\n\n")

        f.write("## Diagnosis\n")
        f.write(f"{sim_output.get('diagnosis', '')}\n\n")

        f.write("## Recommended Actions\n")
        actions = sim_output.get("strategic_actions", [])
        if actions:
            for i, action in enumerate(actions, 1):
                f.write(f"{i}. {action}\n")
        else:
            f.write("No specific actions recommended.\n")
        f.write("\n")

        f.write("## Forecast\n")
        f.write(f"{sim_output.get('forecast', '')}\n\n")

        f.write("## Commentary\n")
        f.write(f"{sim_output.get('commentary', '')}\n\n")

        score = sim_output.get("simulation_score")
        if score is not None:
            f.write(f"_Confidence Score: {score:.2f}_\n")