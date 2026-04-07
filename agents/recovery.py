from utils.logger import log_step

def recovery(state):
    tasks = state.get("tasks", [])
    issues = state.get("issues", [])

    fixes = []

    for t in tasks:
        if not t.get("deadline") or t.get("deadline") in ["Not specified", ""]:
            fixes.append({
                "task": t.get("task"),
                "problem": "Missing deadline",
                "suggested_fix": "Set deadline within 3 days based on priority"
            })

    if not fixes:
        result = {"fixes": ["No action needed"]}
    else:
        result = {"fixes": fixes}

    log_step("recovery", result)

    return {**state, "recovery": result}