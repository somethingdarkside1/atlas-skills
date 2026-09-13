---
part: build-skill
date: 2026-09-13
status: accepted
---

# A wait for a person is a state on disk, and tasks carry a review status for it

`/review-it` used to wait in chat for the human's word on `(you)` boxes, `/build-it` used to loop on `Next: /build-it` when it needed an answer, and nothing on disk said a task was waiting for review, so `/atlas go` and a parked session could not tell. Now a task has four statuses (todo, doing, review, done), `/build-it` moves a task to review when Delivered is written and sends a missing answer to the map as an open question, and `/review-it` leaves unticked `(you)` boxes for the human to tick in the file and ends with a `Next:` line. Rounds and the prototype verdict remain conversations, because they are the point of those skills.

Considered: a dated Delivered line so review could compare dates (fragile, and still nothing for `go` to read); keeping the chat wait and telling `go` to stop there (the state dies with the session).
Revisit when: a tracker cannot express a fourth state.
