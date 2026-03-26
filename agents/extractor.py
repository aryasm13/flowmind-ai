from utils.llm import call_llm
from utils.logger import log_step
import json

def extractor(state):
    text = state.get("input", "")

    prompt = f"""
Extract tasks.

Return ONLY JSON:
[
  {{"task":"...","owner":"...","deadline":"..."}}
]

Text: {text}
"""

    result = call_llm(prompt)
    try:
        if isinstance(result, str):
            result = json.loads(result)
        if not isinstance(result, list):
            raise Exception()
    except:
        result = [
            {
                "task": "General task",
                "owner": "Unassigned",
                "deadline": "Not specified"
            }
        ]

    log_step("extractor", result)

    return {**state, "tasks": result}