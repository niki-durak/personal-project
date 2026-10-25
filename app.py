from flask import Flask, render_template, request, redirect, url_for
from tracker import list_expenses, total
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
        expenses.append((category, float(amount)))
        save_to_json(expenses)
        return redirect("/tracker")
    return render_template("tracker.html", items=expenses, total=t)

if __name__ == "__main__":
    app.run(debug=True)