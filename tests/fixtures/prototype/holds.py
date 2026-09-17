"""PROTOTYPE, throw away.

Question: under the proposed hold rule, can a returned book sit on the shelf
while a member is still waiting for it?
Kind: a behavior the agent can measure.
Answer yes if any reachable state has the book on the shelf and someone in the
queue. Answer no if no such state appears within the bound.
Bound: one sitting; members Ana, Ben, and Cy; every sequence of up to 6 actions.

Proposed rule: a returned book is offered to the first member waiting. That
member can collect it or cancel. A cancel while the book is on offer puts the
book back on the shelf.

Run: python3 holds.py            (the proposed rule)
     python3 holds.py pass-on    (a cancel passes the offer to the next member)
"""
import sys
from collections import deque

MEMBERS = ("Ana", "Ben", "Cy")


class Refused(Exception):
    pass


def start():
    return {"loaned_to": "Ana", "offered_to": None, "shelf": False, "queue": ()}


def step(state, action, rule):
    """The rules only: return the next state or raise Refused."""
    kind, member = action
    s = dict(state)
    if kind == "hold":
        if s["shelf"]:
            raise Refused("the book is on the shelf, so borrow it instead")
        if member in s["queue"] or member == s["loaned_to"]:
            raise Refused(f"{member} already has the book or a hold")
        s["queue"] += (member,)
    elif kind == "borrow":
        if not s["shelf"]:
            raise Refused("the book is not on the shelf")
        s["shelf"], s["loaned_to"] = False, member
    elif kind == "return":
        if s["loaned_to"] is None:
            raise Refused("nobody has the book")
        s["loaned_to"] = None
        if s["queue"]:
            s["offered_to"] = s["queue"][0]
        else:
            s["shelf"] = True
    elif kind == "collect":
        if s["offered_to"] != member:
            raise Refused(f"the book is not on offer to {member}")
        s["loaned_to"], s["offered_to"], s["queue"] = member, None, s["queue"][1:]
    elif kind == "cancel":
        if member not in s["queue"]:
            raise Refused(f"{member} has no hold")
        s["queue"] = tuple(m for m in s["queue"] if m != member)
        if s["offered_to"] == member:
            s["offered_to"] = None
            if rule == "pass-on" and s["queue"]:
                s["offered_to"] = s["queue"][0]
            else:
                s["shelf"] = True
    return s


def describe(s):
    return (f"loaned to {s['loaned_to'] or 'nobody'} | on offer to {s['offered_to'] or 'nobody'} | "
            f"on shelf {'yes' if s['shelf'] else 'no'} | waiting: {', '.join(s['queue']) or 'nobody'}")


def walk(title, actions, rule):
    print(f"\n{title}\n  start: {describe(start())}")
    state = start()
    for action in actions:
        name = " ".join(x for x in action if x)
        try:
            state = step(state, action, rule)
            print(f"  {name}: {describe(state)}")
        except Refused as reason:
            print(f"  {name}: refused, {reason}")


def search(rule, depth):
    """Breadth first over every legal sequence of up to `depth` actions."""
    choices = [("return", None)] + [(k, m) for m in MEMBERS for k in ("hold", "borrow", "collect", "cancel")]
    frontier, sequences = deque([(start(), [])]), 0
    while frontier:
        state, path = frontier.popleft()
        if state["shelf"] and state["queue"]:
            return path, sequences
        if len(path) < depth:
            for action in choices:
                try:
                    frontier.append((step(state, action, rule), path + [action]))
                    sequences += 1
                except Refused:
                    pass
    return None, sequences


rule = sys.argv[1] if len(sys.argv) > 1 else "proposed"
print(f"Rule: {rule}")
walk("Normal path", [("hold", "Ben"), ("return", None), ("collect", "Ben")], rule)
walk("Awkward edge", [("hold", "Ben"), ("hold", "Cy"), ("return", None), ("cancel", "Ben")], rule)
walk("Should be refused", [("return", None), ("hold", "Ben"), ("collect", "Cy")], rule)
found, sequences = search(rule, 6)
if found:
    print(f"\nStopped after {sequences} legal sequences: the book is on the shelf while someone waits.")
    print("Shortest case: " + ", ".join(" ".join(x for x in a if x) for a in found))
else:
    print(f"\nChecked all {sequences} legal sequences of up to 6 actions.")
    print("No state had the book on the shelf while someone waits.")
