# modules/output_formatter.py

def pretty_print_simulation_output(response):
    print("\n=== SIMULATION DIAGNOSIS ===")
    print(response.get("diagnosis", "N/A"))
    print("\n=== STRATEGIC ACTIONS ===")
    for i, action in enumerate(response.get("strategic_actions", []), 1):
        print(f"{i}. {action}")
    print("\n=== FORECAST ===")
    print(response.get("forecast", "N/A"))
    print("\n=== COMMENTARY ===")
    print(response.get("commentary", "N/A"))
    print("\n=== SIMULATION SCORE ===")
    print(f"{response.get('simulation_score', 'N/A'):.2f}")