## Self-review of Personas and Wireframes

Screen 1 | Frames: join-phone, join-laptop

**Works well:** The form has three fields and one big "Join the queue" button, so Swaegg can tell what to do within 5 seconds and has little to type on a phone. This follows Swaegg rule 2 (one main action per screen) and rule 3 (loads fast, no large images or heavy scripts).

**Problem:** Error prevention. Nothing shows what happens if the number of members is blank or not a number, or if the same family joins twice. The labels and placeholders are also fairly small for Swaegg, who says small font is a problem (rule 1).

**Change (kept):** I am keeping the layout. Three fields and one button is the simplest form that still meets FR-01, and adding helper text or more elements would work against Swaegg rule 2. The placeholder "e.g. 4" already shows the expected format. Error messages are not a layout decision, so I will add them in the HTML (for example, "Please enter a number") and check for blank fields before joining. I will use a large base font for labels and inputs in Part 4. I am also keeping the single "Purok and time slot" dropdown because splitting it into two fields would add a step, and families already say "Purok 2, 9:00 AM" as one thing.

---

Screen 2 | Frames: my-place-phone, my-place-laptop

**Works well:** The ticket number (#12) is the largest thing on screen, followed by the status and "5 families ahead", so Swaegg sees what he needs first, even from far away on the phone. This follows Swaegg rule 1 (large ticket number and status) and his goal of knowing when it is his family's turn.

**Problem:** Visibility of system status. Swaegg has little or no mobile data and loses signal when the power goes out, so "Updated just now (refreshes by itself)" could be false and he could miss being called. The wireframe also only shows the WAITING state.

**Change (kept):** I am keeping the layout because the order (ticket, status, position, time slot) already matches what Swaegg needs first. I will build the called state that uses the same status frame, only with different text. I will build it in the HTML and make it big and obvious. In the build, the note will show the real time ("Last updated 9:12 AM") and change to a "No connection..." message when a refresh fails, instead of always saying "just now". I am not adding a refresh button because Swaegg wants a screen with no distracting buttons (rule 2).

---

Screen 3 | dashboard-phone, dashboard-laptop

**Works well:** Each row shows the family's name, purok and time slot with Received and No-show beside it, and "Call next family" sits big at the top. This follows Rea rule 1 (only the list, names, time slots and action buttons), rule 3 (she can find a family by name and time slot without a ticket) and her goal of working with one hand while busy.

**Problem:** Rea rule 2 asks to show clearly who already received. The wireframe only shows waiting families, so once a row is marked Received it is not clear how it will look. Received and No-show are also the same size side by side, so a wrong tap is possible.

**Change (kept):** I am keeping the layout. The row already has a status word ("waiting"), so marking a family changes that word to "received" or "no-show" and the row is greyed out. That meets rule 2 without adding any new elements, and I will keep received rows visible in the list so duplicate claims can be seen. I am keeping Received and No-show at the same large size because are easier to hit with one free hand. A wrong mark can be fixed by changing the status again. Rea call a specific family when someone arrives outside their slot or lost their ticket, which is the situation in her scenario.