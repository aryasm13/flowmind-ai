from utils.logger import log_step

def recovery(state):
    issues = state.get("issues", [])
    tasks = state.get("tasks", [])

    fixes = []

    for t in tasks:
        if not t.get("deadline") or t.get("deadline") == "Not specified":
            fixes.append({
                "task": t.get("task"),
                "problem": "Missing deadline",
                "suggested_fix": "Assign deadline within 2-3 days based on priority"
            })

    log_step("recovery", fixes)

    return {**state, "recovery": fixes}