import os
from langchain.tools import tool
from dotenv import load_dotenv
import os
from langchain_tavily import TavilySearch
from langchain_google_community import GooglePlacesTool, GooglePlacesAPIWrapper 

load_dotenv()

try:
    google_api_key = os.environ.get("GPLACES_API_KEY")
    places_wrapper = GooglePlacesAPIWrapper()
    places_tool = GooglePlacesTool(api_wrapper=places_wrapper)
except: pass


@tool
def search_attractions(place:str) -> str:
    """Search attractions of a place"""
    try:
        attraction_result = places_tool.run(f"top attractive places in and around {place}")
        if attraction_result:
            return f"Following are the attractions of {place} as suggested by google: {attraction_result}"
    except Exception as e:
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"top attractive places in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            result = result["answer"]
        return f"Google cannot find the details due to {e}. \nFollowing are the attractions of {place}: {result}" 

@tool
def search_restaurants(place:str) -> str:
    """Search restaurants of a place"""
    try:
        restaurants_result = places_tool.run(f"what are the top 10 restaurants and eateries in and around {place}?")
        if restaurants_result:
            return f"Following are the restaurants of {place} as suggested by google: {restaurants_result}"
    except Exception as e:
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"what are the top 10 restaurants and eateries in and around {place}."})
        if isinstance(result, dict) and result.get("answer"):
            result = result["answer"]
        return f"Google cannot find the details due to {e}. \nFollowing are the restaurants of {place}: {result}" 

@tool
def search_activities(place:str) -> str:
    """Search activities of a place"""
    try:
        restaurants_result = places_tool.run(f"Activities in and around {place}")
        if restaurants_result:
            return f"Following are the activities in and around {place} as suggested by google: {restaurants_result}"
    except Exception as e:
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"activities in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            result = result["answer"]
        return f"Google cannot find the details due to {e}. \nFollowing are the activities of {place}: {result}" 

@tool
def search_transportation(place:str) -> str:
    """Search transportation of a place"""
    try:
        restaurants_result = places_tool.run(f"What are the different modes of transportations available in {place}")
        if restaurants_result:
            return f"Following are the modes of transportation available in {place} as suggested by google: {restaurants_result}"
    except Exception as e:
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"What are the different modes of transportations available in {place}"})
        if isinstance(result, dict) and result.get("answer"):
            result = result["answer"]
        return f"Google cannot find the details due to {e}. \nFollowing are the modes of transportation available in {place}: {result}" 
    


places_search_tools_list = [
    search_attractions,
    search_restaurants,
    search_activities,
    search_transportation
]