from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from langgraph.prebuilt import ToolNode, tools_condition

load_dotenv()

tavily = TavilySearch(max_results=2)

def mul(a: int, b: int) -> int:
    """Multiply a and b
    Args:
        a (int): First number
        b (int): Second number
    Returns:
        int: The product of a and b
    """
    return a * b


tools = [tavily, mul]

llm = ChatGroq(model="llama3-8b-8192")
llm.bind_tools(tools)

class State(TypedDict):
    messages: Annotated[list, add_messages]

def chat(state: State):
    return {'messages': [llm.invoke(state['messages'])]}

graph = StateGraph(State)

graph.add_node(chat)
graph.add_node(ToolNode(tools))

graph.add_edge(START, 'chat')
graph.add_conditional_edges('chat', tools_condition)
graph.add_edge('tools', 'chat')

basic_react_gr = graph.compile()