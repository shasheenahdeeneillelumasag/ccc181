# Usability test and Improvement

## 10a. Test with a real user
| | |
| --- | --- |
| **Participant** | Blue |
| **Matches persona** | Matches Swaegg's persona because he experienced in getting relief goods |
| **Setting / relation** | An acquaintance who lined up for relief goods before. Not a CCC181 classmate. |
| **Date and method** | October 24, 2026 through voice call and screen recording |
| **Device** | My laptop |
| **Permission** | Yes, he agreed to the test |


### Note: 
- My participant played both roles: the family that wants relief goods, and the staff member. 
- I ran task 1, then task 3, then task 2. My participant needed the staff action first, so that they could see their own ticket change on My place. In task 2, they watched their My place page after the staff action.

### Results by task

| Task | Did they finish it? (yes / with help / no | About how long it took | Where they hesitated, what they said, and anything that surprised me|
| --- | --- | --- | --- |
| 1. "You just arrived at the barangay hall to get relief goods. Get in line for your barangay and get a ticket."| Yes | About 57 seconds | He wondered because his barangay was not in the dropdown. There was no option for it. |
| 2. "You are waiting now. How many families/people are ahead of you? What is your ticket number?" | Yes | About 1 minute 19 seconds | He did not hesitate. He noticed right away that the status changed on their My place page. He directly saw his ticket number 4 then a status that 1 person ahead of you. |
| **3** | Yes | About 1 minute 57 seconds | He did not hesitate. He explained what he could do on the staff dashboard and said he could use the filter. |

### Which of your persona's "Because …, my interface must …" rules held up, and which did not?


| Rule | Held up? | Test |
| --- | --- | --- |
| **Swaegg:** Because Swaegg says small font is problem, my interface must show the ticker number and status in large text. | Yes | Blue could easily see the ticket number and status. |
| **Swaegg:** Because he wants a screen that is simple with no distracting buttons, my interface must have only one main action on each screen. | Mostly | Blue did not mention it, but he found every element easily. |
| **Swaegg:** Because his family has no mobile data, my interface must load fast and work without large images or heavy scripts. | No | I did not test it without internet. |
| **Rea:** Because Rea wants a straightforward screen with clear, essential information, my interface must show only the waiting list, names, time slots, and the action buttons on the staff dashboard, with nothing extra. | Yes | Blue saw all the elements and did not hesitate. |
| **Rea:** Because her main goal is to stop duplicate claims, my interface must let her mark a family as received in one tap and show clearly who already received. | Partly | Blue never mentioned about duplicate claims but received takes one tap. He also mentioned that he can see that the person/family that is marked received/no-show leaves the list in the table. |
| **Rea:** Because people may arrive outside their time slot or lose their ticket, my interface must show each family's name and time slot in the list, so she can find them without the ticket. | Partly | They did not mention it, but the name and time slot are visible in the list. |

## 10b. Make one improvement

**Most serious problem found:** The most serious problem I found is that position in line status. It was not clear. My place only counted families that were still waiting ahead of the person. When staff clicked 'Call', that family stopped being counted, even though they had not received their goods yet. So the number dropped too early. Also, a ticket with the status 'Called' did not show how many people were ahead at all.

**My fix:** The count now includes families that are waiting or called, so it only goes down when staff mark a family as received or no-show. My place now shows the people ahead for both Waiting and Called tickets. I changed the count in `app.py`.

| Before | After |
| --- | --- |
| ![Before](screenshots/screenshot-before.png) | ![After](screenshots/screenshot-after.png) |