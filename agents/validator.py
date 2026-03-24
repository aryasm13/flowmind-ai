from utils.logger import log_step

def validator(state):
    execution = state["execution"]

    issues = []

    tasks = execution.get("executed", [])

    for task in tasks:
        if not task.get("task"):
            issues.append("Missing task name")

        if not task.get("steps"):
            issues.append("Missing steps")

    # Check deadline
    original_tasks = state.get("tasks", [])
    for t in original_tasks:
        if not t.get("deadline"):
            issues.append("Missing deadline")

    if issues:
        result = {"status": "FAIL", "issues": issues}
    else:
        result = {"status": "PASS", "issues": []}

    log_step("validator", result)

    return {**state, **result}