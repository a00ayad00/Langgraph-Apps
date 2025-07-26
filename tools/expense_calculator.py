from langchain.tools import tool

@tool
def estimate_total_hotel_cost(price_per_night:str, total_days:float) -> float:
    """Calculate total hotel cost"""
    return price_per_night * total_days

@tool
def calculate_total_expense(*costs: float) -> float:
    """Calculate total expense of the trip"""
    return sum(costs)

@tool
def calculate_daily_expense_budget(total_cost: float, days: int) -> float:
    """Calculate daily expense"""
    return total_cost / days if days > 0 else 0


expense_calculator_tools_list = [
    estimate_total_hotel_cost,
    calculate_total_expense,
    calculate_daily_expense_budget
]