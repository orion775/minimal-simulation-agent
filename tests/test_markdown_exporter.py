import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.markdown_exporter import export_simulation_to_markdown

def test_export_simulation_to_markdown(tmp_path):
    sim_output = {
        "diagnosis": "Test diagnosis.",
        "strategic_actions": ["Action one", "Action two"],
        "simulation_score": 0.88
    }
    md_file = tmp_path / "test_output.md"
    export_simulation_to_markdown(sim_output, filename=str(md_file))
    text = md_file.read_text(encoding="utf-8")
    assert "# Simulation Result" in text
    assert "Test diagnosis." in text
    assert "1. Action one" in text
    assert "2. Action two" in text
    assert "0.88" in text
