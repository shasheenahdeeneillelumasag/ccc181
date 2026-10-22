"""CCC181 Week 2: a "Hello, Flask" starter app.

Run it with:
    flask --app app run --debug
then open http://127.0.0.1:5000
"""
from flask import Flask, render_template, flash

app = Flask(__name__)
from flask import Flask, abort, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "dev-only-change-me"  # Week 11 moves this into an environment variable

# Time slots by purok. Change the names and times to match your barangay.
SERVICES = [
    {"id": 1, "Barangay Tibanga": "Purok 1 (8:00 AM)"},
    {"id": 2, "Barangay Dalipuga": "Purok 2 (9:00 AM)"},
    {"id": 3, "Barangay Hinaplanon": "Purok 3 (10:00 AM)"},
]


TICKETS = [
    {"number": 1, "name": "Nena Santos", "household_size": 5, "service_id": 1, "status": "waiting"},
    {"number": 2, "name": "Ben Reyes", "household_size": 3, "service_id": 2, "status": "waiting"},
    {"number": 3, "name": "Rosa Cruz", "household_size": 4, "service_id": 2, "status": "called"},
]

@app.route("/")
def index():
    # render_template looks inside the templates/ folder and passes
    # keyword arguments to the template as variables.
    return render_template("index.html")

@app.route("/queue/<int:ticket_id>")
def ticket(ticket_id):
    # <int:ticket_id> only matches numbers, so /queue/abc returns 404.
    return render_template("ticket.html", ticket_id=ticket_id)

@app.route("/hello")
def hello():
    # The plain-string version from the Routes slide.
    return "Hello, ReliefQ!"

if __name__ == "__main__":
    # Lets you also start the app with: python app.py
    app.run(debug=True)

@app.route("/join")
def join_form():
    return render_template("join.html")

@app.route("/staff")
def staff_dashboard():
    return "Staff dashboard coming soon"