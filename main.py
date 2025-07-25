from modules.prompt_builder import build_prompt
from modules.simulation_engine import simulate_gpt_response
from modules.output_formatter import pretty_print_simulation_output
from modules.version import get_version
from modules.markdown_exporter import export_simulation_to_markdown
from modules.memo_generator import export_simulation_memo
from modules.context import domain_context
import json
import argparse

def get_user_input():
    parser = argparse.ArgumentParser(description="Minimal Simulation Agent")

    parser.add_argument("--scenario", type=str, help="Simulation scenario")
    parser.add_argument("--goal", type=str, help="Goal")
    parser.add_argument("--constraint", type=str, help="Constraint")
    parser.add_argument("--domain", type=str, help="Domain profile to use")
    parser.add_argument("--export-json", action="store_true", help="Export output to a JSON file")
    parser.add_argument("--export-md", action="store_true", help="Export output to a Markdown file")
    parser.add_argument("--export-memo", action="store_true", help="Export memo report to Markdown")
    args = parser.parse_args()

    # Fallback to interactive input
    scenario = args.scenario or input("Enter scenario: ")
    goal = args.goal or input("Enter goal: ")
    constraint = args.constraint or input("Enter constraint: ")

    # Only update domain if explicitly passed in
    if args.domain:
        domain_context["active_domain"] = args.domain

    return {
        "scenario": scenario,
        "goal": goal,
        "constraint": constraint,
        "domain": args.domain,
        "export_json": args.export_json,
        "export_md": args.export_md,
        "export_memo": args.export_memo,
    }

def main():
    user_data = get_user_input()

    prompt = build_prompt(
        user_data["scenario"],
        user_data["goal"],
        user_data["constraint"],
    )

    response = simulate_gpt_response(
        prompt,
        scenario=user_data["scenario"],
        goal=user_data["goal"],
        constraint=user_data["constraint"]
    )

    pretty_print_simulation_output(response)

    # Always export to JSON
    with open("simulation_output.json", "w", encoding="utf-8") as f:
        json.dump(response, f, indent=2)
    print("Simulation output saved to simulation_output.json")

    if user_data.get("export_md"):
        export_simulation_to_markdown(response)
        print("Simulation output saved to simulation_output.md")

    # Always export memo
    scenario_text = f"{user_data['scenario']} Goal: {user_data['goal']}. Constraint: {user_data['constraint']}."
    export_simulation_memo(response, scenario_text=scenario_text)
    print("Simulation memo saved to simulation_memo.md")

if __name__ == "__main__":
    main()
