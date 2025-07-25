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
Forecast: Likely to attract offers if adjusted promptly.
Commentary: Seller resistance is delaying outcomes.
Simulation Score: 0.72
    '''
    parsed = parse_gpt_output(gpt_output)
    assert parsed["diagnosis"]
    assert isinstance(parsed["strategic_actions"], list) and len(parsed["strategic_actions"]) > 0
    assert parsed["forecast"]
    assert parsed["commentary"]
    assert isinstance(parsed["simulation_score"], float)