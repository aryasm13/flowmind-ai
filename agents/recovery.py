from utils.logger import log_step

def recovery(state):
    status = state["status"]

    if status == "FAIL":
        issues = state.get("issues", [])

        fixes = []

        for issue in issues:
            if "deadline" in issue:
                fixes.append("Add deadline to tasks")
            elif "steps" in issue:
                fixes.append("Add execution steps")
            elif "task" in issue:
                fixes.append("Define task clearly")

        result = {"fixes": fixes}

    else:
        result = {"fixes": ["No action needed"]}

    log_step("recovery", result)

    return {**state, "recovery": result}