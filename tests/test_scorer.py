import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.scorer import calculate_simulation_score

def test_calculate_simulation_score():
    s1 = calculate_simulation_score(
        "Luxury home unsold for 12 months", "Secure offer", "Do not reduce"
    )
    s2 = calculate_simulation_score(
        "", "", ""
    )
    assert 0.5 <= s1 <= 0.95
    assert 0.5 <= s2 <= 0.95
    assert isinstance(s1, float)