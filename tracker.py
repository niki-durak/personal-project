def add_expense(expenses: list, amount, category: str):
    expenses.append((category, amount))

def delete_expense(expenses: list, index: int):
    try:
        expenses.pop(index)
    except IndexError:
        return
def list_expenses(expenses: list):
    a = ''
    for category, amount in expenses:
        a += f'{category} - {amount}\n'
    return a[0:-1]

def total_by_category(expenses: list):
    d = {}
    for category, amount in expenses:
        if category not in d:
            d[category] = amount
        else:
            d[category] += amount
    return d

def total(expenses: list):
    result = 0
    for category, amount in expenses:
        result += amount
        result = round(result, 2)
    return result