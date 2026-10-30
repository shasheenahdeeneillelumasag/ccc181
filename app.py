"""ReliefQ: relief goods queue system

Run it with:
    flask --app app run --debug
then open http://127.0.0.1:5000
"""

import os
from datetime import time, timedelta, timezone

from dotenv import load_dotenv
from flask import Flask, abort, flash, redirect, render_template, request, url_for
from flask_migrate import Migrate
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError

from models import Barangay, Family, Ticket, db

load_dotenv()

app = Flask(__name__)
app.secret_key = "dev-only-change-me"  # Week 11 moves this into an environment variable
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
app.config["SQLALCHEMY_ECHO"] = os.environ.get("SQLALCHEMY_ECHO") == "1"

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    # render_template looks inside the templates/ folder and passes
    # keyword arguments to the template as variables.
    return render_template("index.html")

PH_TIME = timezone(timedelta(hours=8))  # Philippine time has no daylight saving


@app.template_filter("local")
def local_time(value):
    """Show a database time in Philippine time, e.g. Oct 26, 08:01 AM."""
    return value.astimezone(PH_TIME).strftime("%b %d, %I:%M %p") if value else ""


@app.get("/queue/<int:ticket_id>")
def ticket(ticket_id):
    t = db.get_or_404(Ticket, ticket_id)
    return render_template("ticket.html", ticket=t, barangay=t.family.barangay,
                           ahead=people_ahead(t))

@app.route("/hello")
def hello():
    # The plain-string version from the Routes slide.
    return "Hello, ReliefQ!"

def all_barangays():
    return db.session.scalars(db.select(Barangay).order_by(Barangay.name)).all()

def people_ahead(t):
    """Count tickets still waiting in the same barangay that joined before t."""
    stmt = (db.select(func.count())
            .select_from(Ticket)
            .join(Family, Ticket.family_id == Family.id)
            .where(Family.barangay_id == t.family.barangay_id,
                   Ticket.status == "waiting",
                   Ticket.created_at < t.created_at))
    return db.session.scalar(stmt)

def clean_name(raw):
    """Trim extra spaces and use the same capitalization."""
    return " ".join(raw.split()).title()

@app.get("/join")
def join_form():
    return render_template("join.html", barangays=active_barangays(), form={})


@app.post("/join")
def join():
    form = request.form
    name = clean_name(form.get("name", ""))
    household_size = form.get("household_size", type=int)
    barangay_id = form.get("barangay_id", type=int)
    barangay = db.session.get(Barangay, barangay_id) if barangay_id else None

    errors = {}
    if not name or len(name) > 100:
        errors["name"] = "Enter the full name of the head of the family."
    if household_size is None or not 1 <= household_size <= 100:
        errors["household_size"] = "Enter how many people are in your family."
    if barangay is None or not barangay.active:
        errors["barangay_id"] = "Choose your barangay and time slot."


    family = None
    if not errors:
        family = db.session.scalar(
            db.select(Family).filter_by(barangay_id=barangay.id, head_name=name)
        )
    if family is not None:
        received = db.session.scalar(
            db.select(Ticket).filter_by(family_id=family.id, status="received")
        )
        open_ticket = db.session.scalar(
            db.select(Ticket).where(
                Ticket.family_id == family.id,
                Ticket.status.in_(("waiting", "called")),
            )
        )
        if received:
            errors["name"] = "This family already received relief goods."
        elif open_ticket:
            errors["name"] = (
                f"This family already has ticket (#{open_ticket.id}). If you are a different "
                "family with the same name, add a short note to your name like 'Purok 2'."
            )

    if errors:
        flash("Please fix the highlighted fields.", "danger")
        return render_template("join.html", barangays=active_barangays(),
                               form=form, errors=errors), 400

    if family is None:
        family = Family(head_name=name, household_size=household_size, barangay=barangay)
    else:
        family.household_size = household_size
    ticket = Ticket(family=family)
    db.session.add(ticket)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        flash("Something went wrong saving your ticket. Please try again.", "danger")
        return render_template("join.html", barangays=active_barangays(),
                               form=form, errors={}), 409

    flash(f"You joined the queue. Your ticket is #{ticket.id}.", "success")
    return redirect(url_for("ticket", ticket_id=ticket.id))

@app.get("/queue/<int:ticket_id>/status.json")
def ticket_status(ticket_id):
    t = db.get_or_404(Ticket, ticket_id)
    return {"status": t.status, "ahead": people_ahead(t)}
    
@app.post("/queue/<int:ticket_id>/leave")
def leave(ticket_id):
    t = db.get_or_404(Ticket, ticket_id)
    if t.status in ("waiting", "called"):
        t.status = "left"  # soft delete: the row stays for reports
        db.session.commit()
    flash("You left the queue.", "info")
    return redirect(url_for("index"))

@app.post("/staff/tickets/<int:ticket_id>/delete")
def delete_ticket(ticket_id):
    t = db.get_or_404(Ticket, ticket_id)
    db.session.delete(t) 
    db.session.commit()
    flash(f"Ticket #{ticket_id} was deleted.", "warning")
    return redirect(url_for("staff_dashboard",
                            service_id=request.form.get("service_id", type=int)))

@app.get("/staff")
def staff_dashboard():
    service_id = request.args.get("service_id", type=int)
    stmt = (db.select(Ticket)
            .join(Family, Ticket.family_id == Family.id)
            .where(Ticket.status.in_(["waiting", "called"]))
            .order_by(Ticket.created_at))
    if service_id:
        stmt = stmt.where(Family.barangay_id == service_id)
    queue = db.session.scalars(stmt).all()

    barangays = all_barangays()
    counts = dict(db.session.execute(
        db.select(Family.barangay_id, func.count(Ticket.id))
        .join(Ticket, Ticket.family_id == Family.id)
        .where(Ticket.status == "waiting")
        .group_by(Family.barangay_id)
    ).all())
    waiting_counts = {b.id: counts.get(b.id, 0) for b in barangays}
    received = db.session.scalar(
        db.select(func.count()).select_from(Ticket).where(Ticket.status == "received"))
    has_waiting = any(t.status == "waiting" for t in queue)

    return render_template("staff.html", queue=queue, services=barangays,
                           selected=service_id, waiting_counts=waiting_counts,
                           received=received, has_waiting=has_waiting)
 
 
@app.post("/staff/call-next")
def call_next():
    barangay_id = request.form.get("service_id", type=int)
    stmt = (db.select(Ticket)
            .where(Ticket.status == "waiting")
            .order_by(Ticket.created_at)
            .limit(1))
    if barangay_id:
        stmt = (stmt.join(Family, Ticket.family_id == Family.id)
                    .where(Family.barangay_id == barangay_id))
    nxt = db.session.scalar(stmt)
    if nxt is None:
        flash("No one is waiting.", "warning")
    else:
        nxt.status = "called"
        nxt.called_at = func.now()
        db.session.commit()
        flash(f"Ticket #{nxt.id} is called.", "info")
    return redirect(url_for("staff_dashboard", service_id=barangay_id))
 
 
STAFF_ACTIONS = {"call": "called", "serve": "received", "no-show": "no-show"}


@app.post("/staff/tickets/<int:ticket_id>/<action>")
def staff_action(ticket_id, action):
    new_status = STAFF_ACTIONS.get(action)
    if new_status is None:
        abort(404)
    t = db.get_or_404(Ticket, ticket_id)
    back = url_for("staff_dashboard", service_id=request.form.get("service_id", type=int))
    if t.status not in ("waiting", "called"):
        flash(f"Ticket #{ticket_id} is already {t.status}, so it cannot be changed.", "warning")
        return redirect(back)
    t.status = new_status
    if new_status == "called":
        t.called_at = func.now()
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        flash("Could not save that change.", "danger")
        return redirect(back)
    flash(f"Ticket #{ticket_id} marked {new_status}.", "info")
    return redirect(back)

@app.cli.command("seed")
def seed():
    """Add the starting barangays if they are not there yet."""
    starting = [
        ("Barangay Tibanga", time(8, 0)),
        ("Barangay Dalipuga", time(9, 0)),
        ("Barangay Hinaplanon", time(10, 0)),
    ]
    for name, slot in starting:
        exists = db.session.scalar(db.select(Barangay).filter_by(name=name))
        if exists is None:
            db.session.add(Barangay(name=name, slot_time=slot))
    db.session.commit()
    print("Barangays are ready.")

def active_barangays():
    stmt = db.select(Barangay).filter_by(active=True).order_by(Barangay.name)
    return db.session.scalars(stmt).all()


def parse_slot(raw):
    try:
        return time.fromisoformat(raw)
    except ValueError:
        return None


@app.post("/staff/services")
def service_create():
    name = request.form.get("name", "").strip()
    slot = parse_slot(request.form.get("slot_time", ""))
    if not name or len(name) > 60 or slot is None:
        flash("Enter a name (up to 60 characters) and a time slot.", "danger")
        return redirect(url_for("services_list"))
    db.session.add(Barangay(name=name, slot_time=slot))
    try:
        db.session.commit()
        flash(f"Barangay “{name}” added.", "success")
    except IntegrityError:
        db.session.rollback()
        flash(f"A barangay named “{name}” already exists.", "danger")
    return redirect(url_for("services_list"))

@app.post("/staff/services/<int:service_id>/edit")
def service_edit(service_id):
    b = db.get_or_404(Barangay, service_id)
    name = request.form.get("name", "").strip()
    slot = parse_slot(request.form.get("slot_time", ""))
    if not name or len(name) > 60 or slot is None:
        flash("Enter a name (up to 60 characters) and a time slot.", "danger")
        return redirect(url_for("services_list"))
    b.name = name
    b.slot_time = slot
    b.active = request.form.get("active") == "on" 
    try:
        db.session.commit()
        flash(f"Barangay “{name}” updated.", "success")
    except IntegrityError:
        db.session.rollback()
        flash(f"A barangay named “{name}” already exists.", "danger")
    return redirect(url_for("services_list"))


@app.post("/staff/services/<int:service_id>/delete")
def service_delete(service_id):
    b = db.get_or_404(Barangay, service_id)
    if b.families:
        flash(f"“{b.name}” has families registered, so it cannot be deleted. Turn it off instead.", "danger")
        return redirect(url_for("services_list"))
    name = b.name
    db.session.delete(b)
    db.session.commit()
    flash(f"Barangay “{name}” deleted.", "warning")
    return redirect(url_for("services_list"))

@app.get("/staff/services")
def services_list():
    counts = dict(db.session.execute(
        db.select(Family.barangay_id, func.count(Ticket.id))
        .join(Ticket, Ticket.family_id == Family.id)
        .group_by(Family.barangay_id)
    ).all())
    return render_template("services.html", barangays=all_barangays(), counts=counts)


if __name__ == "__main__":
    # Lets you also start the app with: python app.py
    app.run(debug=True)