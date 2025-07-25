from modules.prompt_builder import build_prompt
from modules.simulation_engine import simulate_gpt_response
from modules.output_formatter import pretty_print_simulation_output
from modules.version import get_version
from modules.markdown_exporter import export_simulation_to_markdown
import json
import argparse

def get_user_input():
    parser = argparse.ArgumentParser(description="Minimal Simulation Agent")
    parser.add_argument("--scenario", type=str, help="Property scenario")
    parser.add_argument("--goal", type=str, help="Goal")
    parser.add_argument("--constraint", type=str, help="Constraint")
    parser.add_argument("--export-json", action="store_true", help="Export output to a JSON file")
    parser.add_argument("--export-md", action="store_true", help="Export output to a Markdown file")
    args = parser.parse_args()

    scenario = args.scenario or input("Enter scenario: ")
    goal = args.goal or input("Enter goal: ")
    constraint = args.constraint or input("Enter constraint: ")

    return {
        "scenario": scenario,
        "goal": goal,
        "constraint": constraint,
        "export_json": args.export_json,
        "export_md": args.export_md,
    }

def main():
    user_data = get_user_input()
    prompt = build_prompt(
        user_data["scenario"],
        user_data["goal"],
        user_data["constraint"]
    )
    response = simulate_gpt_response(prompt)
    pretty_print_simulation_output(response)
    if user_data.get("export_md"):
        export_simulation_to_markdown(response)
        print("Simulation output saved to simulation_output.md")
    if user_data.get("export_json"):
        with open("simulation_output.json", "w", encoding="utf-8") as f:
            json.dump(response, f, indent=2)
        print("Simulation output saved to simulation_output.json")

if __name__ == "__main__":
    main()