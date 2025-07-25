# ideas.md

# Simulation Engine – Future Ideas & Modularity Overview

## Completed Capabilities

- Modular architecture organized around domain profiles
- Fully decoupled components:
  - Prompt construction
  - GPT response parsing
  - Scoring logic (optional per-domain)
  - Output formatting (CLI, JSON, Markdown memo)
- GPT system prompts are domain-specific and enforced at runtime
- Domain mismatch handling is built into the engine
- Command-line interface supports both scripted and interactive input
- Structured output is always generated in JSON and Markdown

## Future Ideas

### 1. Auto-Select Domain Based on Input
Add logic to infer the appropriate domain based on keywords in the scenario text.  
For example, "CRISPR" might map to science, while "apartment" or "offer" suggests real estate.  
This could be done with simple keyword mapping or light NLP. Manual override with `--domain` would still be available.

### 2. Per-Domain Input Validation
Allow domain profiles to define a function that checks whether the input is relevant.  
This would improve rejection accuracy and avoid sending irrelevant prompts to GPT.  
For example, a science domain could reject anything referencing pricing or properties.

### 3. Add a Test Suite for Domain Handling
Include tests that cover:
- Switching domains using CLI
- Fallback behavior when no domain is passed
- Blocking of out-of-domain input by GPT
- Correct fallback to general scoring when no domain-specific scorer is defined

### 4. Scoring Extensions and Alternatives
Right now, real estate uses a custom scoring function while others fall back to a generic one.  
Future options include:
- Using NLP to understand current situation and risk.
- Pluggable scoring models (domain-specific logic)
- Data-driven heuristics
- ML-based confidence prediction

### 5. Expand to New Domains
New domain profiles can be added easily. Some ideas include:
- Finance (e.g. trading strategy planning, budgeting scenarios)
- Healthcare (e.g. trial design, patient prioritization)
- Startups (e.g. investor pitches, product market fit strategy)

## Modularity and Design Principles

- Each domain is defined in `domain_profiles.py` and can be added or removed independently
- Prompt formatting is built from domain-provided templates
- Domains may define their own scoring functions and input validators
- The simulation engine itself is domain-agnostic
- Export modules work with structured JSON and are unaffected by domain differences
- Adding support for a new domain requires only a profile entry and optional functions

## Summary

This system was designed to be modular and easily extensible. To add a new domain, you only need:
1. A profile definition in `domain_profiles.py`
2. An optional custom scoring function
3. An optional input validator
Everything else integrates automatically.