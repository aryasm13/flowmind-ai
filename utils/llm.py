from groq import Groq
import os
import json
import re
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_json(text):
    try:
        text = re.sub(r"```json|```", "", text)

        # find JSON block
        match = re.search(r"\{.*\}|\[.*\]", text, re.DOTALL)
        if match:
            return json.loads(match.group())

    except:
        pass

    return None  # IMPORTANT change


def call_llm(prompt):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    text = response.choices[0].message.content

    return extract_json(text)