from langgraph.graph import StateGraph

from agents.extractor import extractor
from agents.planner import planner
from agents.executor import executor
from agents.validator import validator
from agents.recovery import recovery


# ---------- ROUTING LOGIC ----------
def route_decision(state):
    """
    Decide next step after validation
    """
    if state.get("status") == "FAIL":
        return "recovery"
    return "__end__"


# ---------- BUILD GRAPH ----------
def build_workflow():
    workflow = StateGraph(dict)

    # Nodes
    workflow.add_node("extractor", extractor)
    workflow.add_node("planner", planner)
    workflow.add_node("executor", executor)
    workflow.add_node("validator", validator)
    workflow.add_node("recovery", recovery)

    # Entry
    workflow.set_entry_point("extractor")

    # Flow
    workflow.add_edge("extractor", "planner")
    workflow.add_edge("planner", "executor")
    workflow.add_edge("executor", "validator")

    # Conditional routing
    workflow.add_conditional_edges(
        "validator",
        route_decision,
        {
            "recovery": "recovery",
            "__end__": "__end__"
        }
    )

    return workflow.compile()


# App instance
app = build_workflow()