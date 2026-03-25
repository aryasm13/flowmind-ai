from utils.llm import call_llm
from utils.logger import log_step

def extractor(state):
    text = state["input"]

    prompt = f"""
Extract tasks.

Return ONLY JSON:
[
  {{"task":"...","owner":"...","deadline":"..."}}
]

Text: {text}
"""

    result = call_llm(prompt)

# SAFE FALLBACK
    if not result or isinstance(result, dict):
        result = [
            {
                "task": "General task",
                "owner": "Unassigned",
                "deadline": "Not specified"
            }
        ]

        log_step("extractor", result)

    return {**state, "tasks": result}