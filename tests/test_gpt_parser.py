import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.gpt_parser import parse_gpt_output

def test_parse_gpt_output():
    gpt_output = '''
Diagnosis: The current guide price is too high for current buyer interest.
Strategic Actions:
- Reduce asking price to £4.25M
- Launch targeted marketing to international buyers
- Switch agents if no progress in 14 days
Simulation Score: 0.72
    '''
    parsed = parse_gpt_output(gpt_output)
    assert parsed["diagnosis"].startswith("The current guide price")
    assert "Reduce asking price" in parsed["strategic_actions"][0]
    assert abs(parsed["simulation_score"] - 0.72) < 1e-6