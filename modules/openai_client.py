import os
from modules.domain_profiles import DOMAIN_PROFILES

def query_openai_gpt(prompt, domain):
    import os
    from openai import OpenAI
    from modules.domain_profiles import DOMAIN_PROFILES

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("No OpenAI API key found in OPENAI_API_KEY environment variable.")

    client = OpenAI(api_key=api_key)

    # Use correct domain profile's system prompt
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