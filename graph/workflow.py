from langgraph.graph import StateGraph

from agents.extractor import extractor
from agents.planner import planner
from agents.executor import executor
from agents.validator import validator
from agents.recovery import recovery

def route_decision(state):
    return "recovery" if state["status"] == "FAIL" else "__end__"

def build_workflow():
    workflow = StateGraph(dict)

    workflow.add_node("extractor", extractor)
    workflow.add_node("planner", planner)
    workflow.add_node("executor", executor)
    workflow.add_node("validator", validator)
    workflow.add_node("recovery", recovery)

    workflow.set_entry_point("extractor")

    workflow.add_edge("extractor", "planner")
    workflow.add_edge("planner", "executor")
    workflow.add_edge("executor", "validator")

    workflow.add_conditional_edges(
        "validator",
        route_decision,
        {
            "recovery": "recovery",
            "__end__": "__end__"
        }
    )

    return workflow.compile()