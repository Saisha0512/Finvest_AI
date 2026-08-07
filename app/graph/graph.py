# Wires nodes into: classify → route → act → respond.

from langgraph.graph import StateGraph, END
from .state import AgentState
from . import nodes


def route_on_intent(state: AgentState) -> str:
    return state["intent"]


def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("classify", nodes.classify_node)
    graph.add_node("policy_qa", nodes.policy_node)
    graph.add_node("portfolio_balance", nodes.portfolio_node)
    graph.add_node("watchlist", nodes.watchlist_node)
    graph.add_node("goals", nodes.goals_node)
    graph.add_node("transactions", nodes.transactions_node)
    graph.add_node("off_topic", nodes.off_topic_node)

    graph.set_entry_point("classify")
    graph.add_conditional_edges("classify", route_on_intent, {
        "policy_qa": "policy_qa",
        "portfolio_balance": "portfolio_balance",
        "watchlist": "watchlist",
        "goals": "goals",
        "transactions": "transactions",
        "off_topic": "off_topic",
    })
    for node in ["policy_qa", "portfolio_balance", "watchlist", "goals", "transactions", "off_topic"]:
        graph.add_edge(node, END)

    return graph.compile()


agent_graph = build_graph()