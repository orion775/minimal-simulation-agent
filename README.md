# Minimal Simulation Agent

# Minimal Simulation Agent

**Version:** v1.1.0

A modular, production-grade simulation engine for strategy generation—fully powered by OpenAI GPT.

## Features

- Accepts scenario, goal, and constraint via CLI or arguments
- Returns structured JSON (diagnosis, strategic actions, forecast, commentary, simulation score)
- Clean modular code: prompt builder, output formatter, parser, markdown and JSON export
- Real GPT-powered output—no hardcoded or dummy data
- Easily adaptable to other domains
- Pytest-based test suite for all modules
- Markdown and JSON export via CLI flags

## How to Run

**Interactive:**
```bash
python main.py or 
python main.py --scenario "£5.25M Knightsbridge townhouse unsold for 9 months" --goal "Secure offer within 60 days" --constraint "Do not reduce below £4.2M" --export-json --export-md

## OpenAI API Key ##

Set your API key in your terminal before running:
PowerShell:$env:OPENAI_API_KEY="sk-your-key-here"

CMD:

set OPENAI_API_KEY=sk-your-key-here