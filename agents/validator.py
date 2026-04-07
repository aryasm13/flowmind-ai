from utils.logger import log_step

def validator(state):
    execution = state.get("execution", {})
    tasks = state.get("tasks", [])

    issues = []

    executed = execution.get("executed", [])

    # -------- Execution checks --------
    for task in executed:
        if not task.get("task"):
            issues.append("Missing task name")

        if not task.get("steps") or len(task.get("steps")) == 0:
            issues.append(f"Task '{task.get('task')}' has no execution steps")

    # -------- Deadline checks --------
    for t in tasks:
        deadline = t.get("deadline")

        if not deadline or deadline in ["Not specified", ""]:
            issues.append(f"Missing deadline for task: {t.get('task')}")

    # -------- Result --------
    if issues:
        result = {
            "status": "FAIL",
            "issues": issues
        }
    else:
        result = {
            "status": "PASS",
            "issues": []
        }

    log_step("status", result)

    return {**state, **result}