import os
from openai import OpenAI

def run_task_agent(user_input: str) -> str:
    client = OpenAI()
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You break down tasks into 3 clear steps."},
            {"role": "user", "content": user_input},
        ],
        max_tokens=200,
    )
    return resp.choices[0].message.content
