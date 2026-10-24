## Swaegg, the person waiting

> "Di na need mulinya physically. Pwede lang muwait sa kilid, then kung imoa nang turn, muduol lang dayon ka [There's no need to line up physically. I can wait on the side, then come up when it's my turn]" (Interview)

| | |
| --- | --- |
| **Photo or sketch** | ![Icon of Swaegg](images/persona1_image.png) |
| **Age, role and background** | 22, male, a 4th year Metallurgical Engineering student in MSU-IIT. Lives in a family of three. Goes with his father to collect relief goods. Uses Facebook and solves problem on his own or with Google. |
| **Goals** | Get the family's relief pack and go home. Don't need to stand in line for too long. Know when it his family's turn. |
| **Frustrations** | Does not know when he can go home because he is not sure when the goods will be given. Some people get called over and insert the line. |
| **Devices and context** | Uses his father's old phone, not a keypad phone. No mobile data, only text. Signal is usually fine, but without electricity there is no signal. Waits at the barangay or church where goods are given. |
| **Tech comfort** | Medium. He uses Facebook and Google and fixes problems on his own. |
| **Accessibility needs** | Small font is hard to read. Little or no mobile data, and no signal when the power is out. Wants a screen that is simple, with no distracting buttons. |

### Scenario

Swaegg goes to the barangay hall with his father because relief goods are being given out today. In the past, the whole family had to stand in a line, and Swaegg never knew when he could go home. This time, his father shows him a ReliefQ System on his phone. he opens it and sees one big number and how many families are ahead of them. He and his father wait on the side, in the shade. When the screen says their turn is called, they walk up, get the pack, and go home.

### Top tasks in the app

| Task | Screen | Requirement ID |
| --- | --- | --- |
| Join the queue and get a ticker number | Join | FR-01 |
| Check how many families are ahead | My place | FR-02 |

### What this means for my interface

1. Because Swaegg says small font is problem, my interface must show the ticker number and status in large text.
2. Because he wants a screen that is simple with no distracting buttons, my interface must have only one main action on each screen.
3. Because his family has no mobile data, my interface must load fast and work without large images or heavy scripts.

---

## Rea, the staff member

> "We simply let the children line up, and we accommodated them based on who arrived first. We did not have a formal queuing system in place." (interview)

| | |
| --- | --- |
| **Photo or sketch** | ![Icon of Rea](images/persona2_image.png) |
| **Age, role and background** | 22, 3rd-year BA Psychology student. Volunteer and working committee member in a youth organization's one-day relief project. |
| **Goals** | Track who already received goods and prevent duplicate claims. Control how many people arrive at the venue at the same time. Resolve problems fairly when someone says they were skipped. |
| **Frustrations** | There is no formal queue, so people line up and are served by who arrived first. More children came than were on the list, so food ran short. She had to do tasks outside her role, such as buying extra food. |
| **Devices and context** | Uses a laptop and printed materials. There is no internet at the site. Records contact details on paper, which she has to keep organized and safe. Busy running a program with games and a reading session while the distribution happens. |
| **Tech comfort** | Medium. She works on the technical team and uses a laptop, but wants an app that is simple and not confusing. |
| **Accessibility needs** | Needs a clear screen with only essential information. Weak or no internet, and a phone battery that can run out. A printed list is still needed as a backup. |

### Scenario

Rea arrives at the venue at 10 AM with the other volunteers to set up. There is no internet, so she brings her laptop and a printed list of the children as a backup. When the program ends, families start to gather for the distribution. Rea opens the ReliefQ staff dashboard and sees the waiting list with each family's name and time slot. When a family arrives, she finds their name, gives them their pack, and taps Received so nobody gets goods twice. When someone arrives outside their time slot or says they lost their ticket, she checks the list and listens to what they say before she decides.

### Top tasks in the app

| Task | Screen | Requirement ID |
| --- | --- | --- |
| See the waiting list with names and time slots | Staff dashboard | FR-03 |
| Call the next family | Staff dashboard | FR-03 |
| Mark a family as received | Staff dashboard | FR-03 |
| Mark a family as no-show | Staff dashboard | FR-03 |

### What this means for my interface

1. Because Rea wants a straightforward screen with clear, essential information, my interface must show only the waiting list, names, time slots, and the action buttons on the staff dashboard, with nothing extra.
2. Because her main goal is to stop duplicate claims, my interface must let her mark a family as received in one tap and show clearly who already received.
3. Because people may arrive outside their time slot or lose their ticket, my interface must show each family's name and time slot in the list, so she can find them without the ticket.