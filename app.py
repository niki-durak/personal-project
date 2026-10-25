from flask import Flask, render_template, request, redirect, url_for
from tracker import list_expenses, total, total_by_category, add_expense, delete_expense
from storage import load_from_json, save_to_json

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello"


@app.route("/tracker", methods=["GET", "POST"])
def tracker():
    expenses = load_from_json("expenses.json")
    t = total(expenses)
    if request.method == "POST":
        category = request.form["category"]
        amount = request.form["amount"]
        if len(category) != 0 and len(amount) != 0:
            add_expense(expenses, float(amount), category)
            save_to_json(expenses)
            return redirect("/tracker")
    tbc = total_by_category(expenses)
    return render_template("tracker.html", items=expenses, total=t, total_by_category=tbc)

@app.route("/delete", methods=["POST"])
def delete():
    expenses = load_from_json("expenses.json")
    index = int(request.form["index"])
    delete_expense(expenses, index)
    save_to_json(expenses)
    return redirect("/tracker")
if __name__ == "__main__":
    app.run(debug=True)