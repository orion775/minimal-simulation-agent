
# Minimal Simulation Agent

## Project Overview

This project is a fully modular and domain-flexible simulation engine designed to generate strategic recommendations using GPT. While the original task focused on real estate, I intentionally designed the system to support a wide range of domains beyond property — including science, finance, and more — with minimal configuration changes.

Each domain is defined in a central `domain_profiles.py` file, where you can provide a custom system prompt, prompt template, and (optionally) a scoring function specific to that domain. If no scoring function is defined, the engine falls back to a generic scoring strategy.

To switch between domains, simply set the `active_domain` value inside the `modules/context.py` file. The engine will then use that domain’s logic for prompt generation, response validation, and scoring.

Importantly, if a scenario is submitted that falls outside of the selected domain’s scope, the engine will respond with a clear message indicating that it cannot handle the input — rather than trying to fabricate a response. This prevents misuse and encourages intentional domain targeting.

Throughout the project, I aimed to avoid hardcoded logic and maximize reusability. I prioritized system agility and modularity over writing domain-specific rules such as real-estate. Ideas for further enhancements are provided in `ideas.md`, and implementation details can be found in `devlog.md`.

This engine is built to evolve — the more domains you add, the more versatile it becomes.

**Version:** v1.3.0

A modular simulation engine for strategic decision-making, powered by OpenAI GPT and your own simulation scoring logic.

---

### Features

- Domain-driven simulation via pluggable profiles
- Supports real GPT interaction with custom system prompts per domain
- Automatic scoring of scenario realism and strategy viability
- Modular components:
  - Prompt builder
  - GPT output parser
  - Scoring logic (general or domain-specific)
  - Output formatting (pretty print, JSON, Markdown, memo)
- Domain-aware input validation and rejection handling
- Full CLI support with flags for domain, exports, and memo

---

## How to Run

**Interactive:**
```bash
python main.py 
or 
python main.py --scenario "£5.25M Knightsbridge townhouse unsold for 9 months" --goal "Secure offer within 60 days" --constraint "Do not reduce below £4.2M" --export-json --export-md
```

## To run all test

Run all tests:
```bash
pytest
```
## OpenAI API Key ##

Set your API key in your terminal before running:

PowerShell:$env:OPENAI_API_KEY="sk-your-key-here"
CMD:set OPENAI_API_KEY=sk-your-key-here
