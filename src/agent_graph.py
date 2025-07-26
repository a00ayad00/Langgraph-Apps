from src.model_loader import ModelLoader
from src.prompts import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.prebuilt import ToolNode, tools_condition
from tools.weather import weather_tools_list
from tools.places_search import places_search_tools_list
from tools.expense_calculator import expense_calculator_tools_list
from tools.currency_converter import currency_converter_tool_list


tools = [
    * weather_tools_list, 
    * places_search_tools_list,
    * expense_calculator_tools_list,
    * currency_converter_tool_list
]

model_loader = ModelLoader()
llm_with_tools = model_loader.load_llm().bind_tools(tools=tools)


def agent_function(state: MessagesState):
    input_question = [SYSTEM_PROMPT] + state["messages"]
    response = llm_with_tools.invoke(input_question)
    return {"messages": [response]}


state = StateGraph(MessagesState)

state.add_node("agent", agent_function)
state.add_node("tools", ToolNode(tools=tools))

state.add_edge(START, "agent")
state.add_conditional_edges("agent", tools_condition)
state.add_edge("tools", "agent")
state.add_edge("agent", END)

graph = state.compile()

with open('graph.png', "wb") as file:
    file.write(graph.get_graph().draw_mermaid_png())