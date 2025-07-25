
# Minimal Simulation Agent

**Version:** v1.2.0

A modular simulation engine for strategic decision-making, powered by OpenAI GPT and your own simulation scoring logic.

---

##  Features

- Accepts scenario, goal, and constraint via CLI or interactive input
- Modular domain system (e.g. `real_estate`, `science`, etc.)
- GPT prompt building and response parsing per domain profile
- Domain-aware error handling (e.g. rejects off-topic input)
- Structured JSON output with:
  - `diagnosis`
  - `strategic_actions`
  - `forecast`
  - `commentary`
  - `simulation_score` (**calculated locally, not by GPT**)
- Markdown export option (`--export-md`)
- JSON always exported to `simulation_output.json`
- Easy to extend: just add a new domain to `domain_profiles.py`
- Full test suite using `pytest`

---

## How to Run

## To run all test

Run all tests:
```bash
pytest
```
## OpenAI API Key ##

Set your API key in your terminal before running:

PowerShell:$env:OPENAI_API_KEY="sk-your-key-here"
CMD:set OPENAI_API_KEY=sk-your-key-here

**Interactive:**
```bash
python main.py or 
python main.py --scenario "£5.25M Knightsbridge townhouse unsold for 9 months" --goal "Secure offer within 60 days" --constraint "Do not reduce below £4.2M" --export-json --export-md
```