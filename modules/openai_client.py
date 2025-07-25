
import os
import openai

def query_openai_gpt(prompt):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("No OpenAI API key found in OPENAI_API_KEY environment variable.")

    try:
        from openai import OpenAI
    except ImportError:
        raise ImportError("The openai package is not installed. Run 'pip install openai'.")

    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are an expert property sales strategist. Respond as an experienced consultant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=400,
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()