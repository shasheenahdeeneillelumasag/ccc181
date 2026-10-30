# ReliefQ requirements

**Setting:** Relief good distribution in barangay, on the days when families come to receive relief packs.

**People who wait:** Families who need relief goods--- Swaegg in docs/week3/personas.md

**People who serve:** Barangay staff/volunteers who run the distribution --- Rea in docs/week3/personas.md

**Problem statement:** Families who need relief goods need a way to know when their turn is without standing in line for hours, because they cannot tell when they can go home, and they are afraid of being skipped.

## Functional requirements

| ID | Requirement | Priority | Stores data? | Status  |
| :--- | :--- | :--- | :--- | :--- |
| FR-01 | A family can join the queue by entering the head of the family's name, the number of family members, and their barangay with its time slot. | Must  | Yes | Built (Week 3)  |
| FR-02 | A family can see their ticket number, status, and how many families/people  are ahead of them. | Must | Yes | Built (Week 3) |
| FR-03 | A family can see their status change within 10 seconds without reloading the page. | Should | Yes  | Built (Week 3) |
| FR-04 | A staff member can call the next waiting family for a barangay | Must | Yes | Built (Week 3) | 
| FR-05 | A staff member can mark a called family as received or no-show | Must | Yes | Built (Week 3) |
| FR-06 | A family can leave the queue before they receive their goods | Must | Yes | Built (Week 3) | 
| FR-07 ★ | A staff member can see which families already received goods, so that no family gets goods twice. | Must | Yes | Built (Week 4) |
| FR-08 | A staff member can add, rename, and switch off a barangay and its time slot. | Must | Yes | Built (Week 4) | 
| FR-09 | A staff member can filter the waiting list by barangay. | Should | No | Built (Week 3) | 
| FR-10 ★ | A staff member can see how many families are waiting in each barangay. | Should | Yes | Built (Week 3) | 
| FR-11 | A staff member can give a ticket number on paper to a family without a phone, so they are not left out | Won't (This Semester) | Yes | Dropped |
| FR-12 ★ | A senior citizen or a person with disability can join a priority lane that is served first. | Should | Yes | Later |
| FR-13 ★ | A family cannot join the queue again while they still have a waiting or called ticket in the same barangay. | Should | Yes | Built (Week 4) |

## Non-functional requirements

| ID | Requirement | Category | Priority |
| --- | --- | --- | --- | 
| NFR-01 | No ticket is lost when the server or the database restarts. | Reliability | Must |
| NFR-02 | Two families can never get the same ticket number, even if they join at the same moment. | Data integrity | Must |
| NFR-03 | Every value is checked in three places: the browser, the server, and the database | Data integrity | Must |
| NFR-04 | My place loads in under 2 seconds on mobile data. | Performance | Should |
| NFR-05 | Every screen scores 90 or higher in the Lighthouse accessibility check. | Accessibility | Must |
| NFR-06 | No password or secret key is stored in the repository. | Security | Must | 
| NFR-07 | The app collects only the name, the number of family members, and their barangay with its time slot. | Privacy | Must | 

## MVP
 - Must Functional requirements: FR-01, FR-02, FR-04, FR-05, FR-06, FR-07, FR-08
 - Must non-functional requirements: NFR-01, NFR-02, NFR-03, NFR-05, NFR-06, NFR-07.

This is the smallest version that still solves the problem wherein a family can join, see their place, and be called. Staff can call families, mark who received goods, and see who already received, so nobody gets goods twice. The data stays safe when the server restarts.

## Out of scope
- Paper tickets for families without a phone. 
- Text messages when the turn is near. It cost money and need extra setup.
- Inventory of relief goods.This is a different problem from the queue.
- Connecting to government beneficiary lists. It is hard to get access, and it is too big for one semester.

## Feedback table
| Who (role only, no full name) | What they said | What I changed |
| --- | --- | --- |
| A person who received relief goods before | "Dili man sya wrong pero like murag na out of place ra.  Ang FR-11. Kay most man gud ani kay more on like application. While kani kay more on kanang convenience sa other people na walay phone. Dili kay sya muconnect sa application." _(It's not wrong, but it just seems a bit out of place. The FR-11. Because most of these are more focused on the application itself. Whereas this one is more about the convenience of other people who don't have a phone. It doesn't really connect to the application)_| I dropped FR-11 from "Later" to "Dropped" and moved it to the out-of-scope list, because it is a paper process and not an app feature. I kept its ID so it is never reused. I kept the other requirements. |   