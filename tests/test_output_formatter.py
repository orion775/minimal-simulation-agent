import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.output_formatter import pretty_print_simulation_output

def test_pretty_print_simulation_output(capsys):
    response = {
        "diagnosis": "Test diagnosis.",
        "strategic_actions": ["Do thing one", "Do thing two"],
        "simulation_score": 0.66
    }
    pretty_print_simulation_output(response)
    out, _ = capsys.readouterr()
    assert "SIMULATION DIAGNOSIS" in out
    assert "Test diagnosis." in out
    assert "1. Do thing one" in out
    assert "2. Do thing two" in out
    assert "0.66" in out
