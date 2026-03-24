from utils.llm import call_llm
from utils.logger import log_step

def planner(state):
    tasks = state["tasks"]

    prompt = f"""
Break tasks into steps.

STRICT:
- Only JSON

Format:
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
    log_step("planner", result)

    return {**state, "steps": result}