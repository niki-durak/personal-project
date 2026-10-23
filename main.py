from tracker import add_expense, list_expenses, total, total_by_category
from storage import load_from_json, save_to_json

def main():
    exp = load_from_json("expenses.json")
    # add_expense(exp, 100, 'food')
    # add_expense(exp, 500, 'food')
    # add_expense(exp, 100, 'house')
    # add_expense(exp, 100.4, 'game')
    print(list_expenses(exp))
    print(total(exp))
    save_to_json(exp)
    print(load_from_json("expenses.json"))


    
if __name__ == "__main__":
    main()