# Devlog



---
# Devlog

---

## v1.1.0 — 2025-07-24

### Added
- Full OpenAI GPT integration for simulation outputs; all agent responses now use real LLM completions
- Parser now extracts: Diagnosis, Strategic Actions, Forecast, Commentary, and Simulation Score from GPT output
- Markdown export (`--export-md`) and JSON export (`--export-json`) options added to CLI
- CLI output now displays all structured fields, matching JSON/Markdown export
- Pluggable architecture—easy to adapt for other domains by changing system prompt/config
- Codebase now has **no hardcoded or simulated outputs** anywhere

### Changed
- Output formatter and exporters updated to use all five GPT-powered fields
- main.py refactored to use argparse flags for all export options
- Error handling improved for missing API key and invalid GPT output

### Removed
- All fallback, dummy, or simulated responses from simulation_engine.py and exporters

### Notes
- **Requires a valid OpenAI API key and account with quota**
- Next ideas: domain profiles for science/finance, input validation, richer error messages

---

## v1.0.0 — 2025-07-24

### Added
- Modular simulation engine with CLI interface (scenario, goal, constraint)
- CLI arguments support and interactive fallback
- Prompt builder module for LLMs
- Output formatter for clean CLI display
- Simulation scoring logic (modular)
- Version tracker (from `version.txt`)
- Full pytest-based test suite for all modules

### Notes
- All logic is modular and tested.
- Next planned feature: OpenAI API integration for real GPT output.

---