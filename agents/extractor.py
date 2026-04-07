from utils.llm import call_llm
from utils.logger import log_step
import json

def extractor(state):
    text = state.get("input", "")

    prompt = f"""
You are an enterprise task extraction agent.

Extract actionable tasks from the input.

RULES:
- Identify task clearly
- Extract owner if mentioned, else "Unassigned"
- Extract deadline if mentioned, else "Not specified"
- Break compound sentences into multiple tasks
- Keep tasks short and precise

Return STRICT JSON ONLY:
[
  {{
    "task": "...",
    "owner": "...",
    "deadline": "..."
  }}
]

Input:
{text}
"""

    result = call_llm(prompt)

    try:
        if isinstance(result, str):
            result = json.loads(result)

        if not isinstance(result, list):
            raise Exception()

    except:
        # fallback (IMPORTANT)
        result = [
            {
                "task": text[:50],
                "owner": "Unassigned",
                "deadline": "Not specified"
            }
        ]

    log_step("extractor", result)

    return {**state, "tasks": result}