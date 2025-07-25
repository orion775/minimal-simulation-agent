import os
from modules.domain_profiles import DOMAIN_PROFILES

def query_openai_gpt(prompt, domain="real_estate"):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("No OpenAI API key found in OPENAI_API_KEY environment variable.")

    try:
        from openai import OpenAI
    except ImportError:
        raise ImportError("The openai package is not installed. Run 'pip install openai'.")

    client = OpenAI(api_key=api_key)

    # Get system prompt from domain profile
    system_prompt = DOMAIN_PROFILES.get(domain, {}).get("system_prompt", "")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        max_tokens=400,
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()