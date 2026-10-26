from datetime import date

def add_expense(expenses: list, category: str, amount):
    today = date.today().isoformat()
    expense = {"category": category, "amount": amount, "date": today}
    expenses.append(expense)
    
def delete_expense(expenses: list, index: int):
    try:
        expenses.pop(index)
    except IndexError:
        return

def list_expenses(expenses: list):
    a = ''
    for expense in expenses:
        a += f'{expense["category"]} - {expense["amount"]}  -  {expense["date"]}\n'
    return a[0:-1]

def total_by_category(expenses: list):
    d = {}
    for expense in expenses:
        if expense["category"] not in d:
            d[expense["category"]] = expense["amount"]
        else:
            d[expense["category"]] += expense["amount"]
    return d

def total(expenses: list):
    result = 0
    for expense in expenses:
        result += expense["amount"]
        result = round(result, 2)
    return result