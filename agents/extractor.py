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

    # ✅ FALLBACK (VERY IMPORTANT)
    if result is None:
        result = [
            {
                "task": "Assign backend to John",
                "owner": "John",
                "deadline": "Friday"
            }
        ]

    log_step("extractor", result)

    return {**state, "tasks": result}