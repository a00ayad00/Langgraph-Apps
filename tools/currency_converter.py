import os
import requests
from langchain.tools import tool
from dotenv import load_dotenv


load_dotenv()

api_key = os.environ.get("EXCHANGE_RATE_API_KEY")
base_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

@tool
def convert_currency(amount:float, from_currency:str, to_currency:str):
    """Convert amount from one currency to another"""
    url = f"{base_url}/{from_currency}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("API call failed:", response.json())
    rates = response.json()["conversion_rates"]
    if to_currency not in rates:
        raise ValueError(f"{to_currency} not found in exchange rates.")
    return amount * rates[to_currency]


currency_converter_tool_list = [convert_currency]