import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_answer(query, contexts):
    # Constructs an LLM prompt that includes the user’s question plus the top k matches.
    prompt = (
        "You are an internal knowledge assistant.\n\n"
        f"Question: {query}\n\n"
        "Context snippets:\n"
    )
    for c in contexts:
        prompt += f"- {c['metadata']['text']}\n"
    prompt += "\nAnswer concisely:"

    # Calls OpenAI’s chat API (e.g. GPT‑4) to generate a concise, human‑readable answer.
    resp = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return resp.choices[0].message.content.strip()
