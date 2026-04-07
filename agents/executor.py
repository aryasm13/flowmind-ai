from utils.logger import log_step

def executor(state):
    steps = state.get("steps", [])

    executed = []

    for item in steps:
        executed.append({
            "task": item.get("task"),
            "steps": item.get("steps", [])
        })

    result = {
        "executed": executed,
        "status": "SIMULATED"
    }

    log_step("executor", result)

    return {**state, "execution": result}