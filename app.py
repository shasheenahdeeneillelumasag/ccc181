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
    {"id": 1, "name": "Barangay Tibanga (8:00 AM)"},
    {"id": 2, "name": "Barangay Dalipuga (9:00 AM)"},
    {"id": 3, "name": "Barangay Hinaplanon (10:00 AM)"},
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

@app.get("/join")
def join_form():
    return render_template("join.html", services=SERVICES, form={})
 
 
@app.post("/join")
def join():
    form = request.form
    name = form.get("name", "").strip()
    household_size = form.get("household_size", type=int)
    service_id = form.get("service_id", type=int)
 
    errors = {}
    if not name:
        errors["name"] = "Enter the name of the head of the family."
    if household_size is None or not 1 <= household_size <= 20:
        errors["household_size"] = "Enter how many people are in your family (1 to 20)."
    if service_id not in [s["id"] for s in SERVICES]:
        errors["service_id"] = "Choose your barangay and time slot."
 
    if errors:
        flash("Please fix the highlighted fields.", "danger")
        return render_template("join.html", services=SERVICES, form=form, errors=errors), 400
 
    number = TICKETS[-1]["number"] + 1 if TICKETS else 1
    TICKETS.append({"number": number, "name": name, "household_size": household_size,
                    "service_id": service_id, "status": "waiting"})
    flash(f"You joined the queue. Your ticket is #{number}.", "success")
    return redirect(url_for("ticket", ticket_id=number))

@app.route("/staff")
def staff_dashboard():
    return "Staff dashboard coming soon"

if __name__ == "__main__":
    # Lets you also start the app with: python app.py
    app.run(debug=True)