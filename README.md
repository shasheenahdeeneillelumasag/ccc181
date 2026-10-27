# ReliefQ

ReliefQ is a queue system for relief goods distribution in a barangay. Families get a ticket with a queue number, so they don't have to line up for hours. Staff can see the waiting list and call the next family. To run it, create a virtual environment, run `pip install -r requirements.txt`, then run `flask --app app run --debug` and open http://127.0.0.1:5000 in your browser.

Requirements: [docs/requirements.md](docs/requirements.md)

Note: the staff dashboard (/staff) has no login yet. Anyone who knows the address can open it. Staff login comes in a later week.

## ★ Features made for relief goods distribution
- **FR-10 (built):** the staff dashboard shows how many families are waiting in each barangay.
- **FR-07 (this week):** staff can see which families already received goods, so no family gets goods twice.
- **FR-13 (this week):** a family cannot join the queue again while they still have a waiting or called ticket in the same barangay.
- **FR-12 (later):** seniors and persons with a disability can join a priority lane that is served first.