# modules/markdown_exporter.py

def export_simulation_to_markdown(sim_output, filename="simulation_output.md"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# Simulation Result\n\n")
        f.write("## Diagnosis\n")
        f.write(f"{sim_output.get('diagnosis', '')}\n\n")
        f.write("## Strategic Actions\n")
        for i, action in enumerate(sim_output.get('strategic_actions', []), 1):
            f.write(f"{i}. {action}\n")
        f.write("\n## Forecast\n")
        f.write(f"{sim_output.get('forecast', '')}\n")
        f.write("\n## Commentary\n")
        f.write(f"{sim_output.get('commentary', '')}\n")
        f.write("\n## Simulation Score\n")
        f.write(f"{sim_output.get('simulation_score', '')}\n")  