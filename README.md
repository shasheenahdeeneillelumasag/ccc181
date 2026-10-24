ReliefQ is a queue system for relief goods distribution in a barangay. Families get a ticket with a queue number, so they don't have to line up for hours. Staff can see the waiting list and call the next family. To run it, create a virtual environment, run `pip install -r requirements.txt`, then run `flask --app app run --debug` and open http://127.0.0.1:5000 in your browser.

Note: the staff dashboard (/staff) has no login yet. Anyone who knows the address can open it. Staff login comes in a later week.

★ Staff feature: the staff dashboard shows how many families are waiting in each barangay and how many families already received relief goods.