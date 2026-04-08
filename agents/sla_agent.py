from utils.logger import log_step

def sla_agent(state):
    tasks = state.get("tasks", [])

    updated_tasks = []

    for t in tasks:
        task = t.copy()

        deadline = task.get("deadline")

        # -------- FIX MISSING DEADLINES --------
        if not deadline or deadline in ["Not specified", ""]:
            task["deadline"] = "Within 3 days"

        # -------- PRIORITY ASSIGNMENT --------
        if "deploy" in task["task"].lower() or "release" in task["task"].lower():
            task["priority"] = "High"
        elif "test" in task["task"].lower():
            task["priority"] = "Medium"
        else:
            task["priority"] = "Low"

        # -------- RISK ASSIGNMENT --------
        if task["priority"] == "High":
            task["risk"] = "High"
        elif task["priority"] == "Medium":
            task["risk"] = "Medium"
        else:
            task["risk"] = "Low"

        updated_tasks.append(task)

    result = {
        "tasks": updated_tasks
    }

    log_step("sla_agent", result)

    return {**state, "tasks": updated_tasks}