# modules/prompt_builder.py

from modules.domain_profiles import DOMAIN_PROFILES
from modules.context import domain_context

def build_prompt(scenario, goal, constraint):
    domain = domain_context["active_domain"]
    profile = DOMAIN_PROFILES.get(domain)
    if not profile:
        raise ValueError(f"Unknown domain: {domain}")
    template = profile["prompt_template"]
    return template.format(scenario=scenario, goal=goal, constraint=constraint)