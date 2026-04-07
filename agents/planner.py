from utils.llm import call_llm
from utils.logger import log_step
import json

def planner(state):
    tasks = state.get("tasks", [])

    prompt = f"""
You are an enterprise workflow planner.

Convert tasks into detailed execution steps.

RULES:
- Each step must be specific and actionable
- Do NOT write generic steps like "Step 1"
- Include real actions (assign, review, test, deploy, coordinate)
- Keep steps realistic for enterprise workflows

Return STRICT JSON:
[
  {{
    "task": "...",
    "steps": ["specific action", "specific action"]
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
                "steps": [
                    "Assign responsible person",
                    "Define execution steps",
                    "Execute task",
                    "Review completion"
                ]
            }
            for t in tasks
        ]

    log_step("planner", result)

    return {**state, "steps": result}