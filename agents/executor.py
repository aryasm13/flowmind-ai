from utils.logger import log_step

def executor(state):
    steps = state.get("steps", [])

    result = {
        "executed": steps,
        "status": "SIMULATED"
    }

    log_step("executor", result)

    return {**state, "execution": result}