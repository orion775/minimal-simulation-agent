from modules.prompt_builder import build_prompt
from modules.simulation_engine import simulate_gpt_response
from modules.output_formatter import pretty_print_simulation_output
from modules.version import get_version
import argparse

def get_user_input():
    parser = argparse.ArgumentParser(description="Minimal Simulation Agent")
    parser.add_argument("--scenario", type=str, help="Property scenario")
    parser.add_argument("--goal", type=str, help="Goal")
    parser.add_argument("--constraint", type=str, help="Constraint")
    args = parser.parse_args()

    # If any argument is missing, prompt interactively
    scenario = args.scenario or input("Enter scenario: ")
    goal = args.goal or input("Enter goal: ")
    constraint = args.constraint or input("Enter constraint: ")

    return {
        "scenario": scenario,
        "goal": goal,
        "constraint": constraint
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

if __name__ == "__main__":
    main()