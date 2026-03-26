from utils.llm import call_llm
from utils.logger import log_step
import json

def planner(state):
    tasks = state.get("tasks", [])

    prompt = f"""
Break tasks into steps.

STRICT JSON:
[
  {{
    "task": "...",
    "steps": ["step1", "step2"]
  }}
]

Tasks:
{tasks}
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
                "task": t.get("task", "Unknown"),
                "steps": ["Step 1", "Step 2"]
            }
            for t in tasks
        ]

    log_step("planner", result)

    return {**state, "steps": result}