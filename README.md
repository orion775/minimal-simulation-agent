# Minimal Simulation Agent

**Version:** v1.0.0

A modular, test-driven simulation engine for property strategy. Accepts scenario, goal, and constraint via CLI or arguments. Builds a GPT-ready prompt, simulates or calls OpenAI’s API, and returns structured JSON.

---

## Features

- Accepts scenario, goal, constraint (CLI arguments or interactive)
- Clean modular code: prompt builder, output formatter, scorer, version tracker
- Returns structured JSON (diagnosis, strategic actions, simulation score)
- Pretty CLI output
- Version tracking
- Pytest-based tests for all modules

---

## How to Run

```bash
python main.py --scenario "£5.25M Knightsbridge townhouse unsold for 9 months" --goal "Secure offer within 60 days" --constraint "Do not reduce below £4.2M"