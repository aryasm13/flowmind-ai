from langgraph.graph import StateGraph

from agents.extractor import extractor
from agents.planner import planner
from agents.executor import executor
from agents.validator import validator
from agents.recovery import recovery
from agents.sla_agent import sla_agent


# ---------- ROUTING ----------
def route_after_validation(state):
    if state.get("status") == "FAIL":
        return "recovery"
    return "__end__"


def route_after_recovery(state):
    return "sla_agent"


def route_after_sla(state):
    return "validator_final"


# ---------- BUILD ----------
def build_workflow():
    workflow = StateGraph(dict)

    # Nodes
    workflow.add_node("extractor", extractor)
    workflow.add_node("planner", planner)
    workflow.add_node("executor", executor)
    workflow.add_node("validator", validator)
    workflow.add_node("recovery", recovery)
    workflow.add_node("sla_agent", sla_agent)

    # NEW final validator (reuse same function)
    workflow.add_node("validator_final", validator)

    # Entry
    workflow.set_entry_point("extractor")

    # Flow
    workflow.add_edge("extractor", "planner")
    workflow.add_edge("planner", "executor")
    workflow.add_edge("executor", "validator")

    # Validator → recovery if fail
    workflow.add_conditional_edges(
        "validator",
        route_after_validation,
        {
            "recovery": "recovery",
            "__end__": "__end__"
        }
    )

    # Recovery → SLA agent
    workflow.add_edge("recovery", "sla_agent")

    # SLA → final validation
    workflow.add_edge("sla_agent", "validator_final")

    return workflow.compile()


app = build_workflow()