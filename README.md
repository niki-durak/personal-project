# Expense Tracker

A small web app for tracking personal expenses, built with Python and Flask.

## Features

- Add and delete an expense with an amount and a category
- View the list of all expenses
- See the total amount spent
- Data is saved to a local JSON file

## Project structure

- `app.py` - Flask web app (routes)
- `tracker.py` - expense logic (add, list, totals)
- `storage.py` - saving and loading data from JSON
- `templates/tracker.html` - HTML page

## How to run

```bash
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install flask
python app.py
```

Then open http://127.0.0.1:5000/tracker in your browser.

## Roadmap

- Replace JSON storage with a SQL database
- Rewrite the API in Go
- Run everything with Docker