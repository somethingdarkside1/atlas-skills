#!/usr/bin/env python3
"""Create fresh scratch projects for Atlas process evaluation.

Run each named skill as a separate invocation. The fixtures contain deliberate
faults and unresolved human criteria; creating them is not an acceptance test.
The destination must not exist. No network or project history is required.
"""
from pathlib import Path
import argparse
import shutil
import subprocess


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("destination", type=Path)
args = parser.parse_args()
src = Path(__file__).resolve().parents[1]
base = args.destination.resolve()
base.mkdir(parents=True, exist_ok=False)

def project(name,part,outcome):
 r=base/name;r.mkdir()
 t=src/'skills/setup-atlas/templates'
 for rel in ('GLOSSARY.md','MAP.md','plan/README.md','notes/README.md','decisions/README.md'):
  p=r/rel;p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(t/rel,p)
 (r/'AGENTS.md').write_text('This is an isolated exercise project. Save local files only. Do not commit, publish, contact anyone, or modify files outside this folder. Preserve unrelated files. Use the supplied Atlas skills explicitly when requested.\n')
 (r/'MAP.md').write_text((r/'MAP.md').read_text().split('# {Project name}')[0]+f'# {name}\n\nA small project.\n\n## {part.title()}\n\nId: {part}\n**Status:** building\n{outcome}\nNeeds: none.\nOpen questions: none.\nDecisions: none.\nPlan: [plan/{part}/](plan/{part}/).\n')
 (r/f'plan/{part}').mkdir()
 (r/f'plan/{part}/brief.md').write_text(f'---\npart: {part}\n---\n\n# {part.title()}\n\n## Problem\nWe need a dependable deliverable.\n\n## Outcome\n{outcome}\n\n## Decisions\nUse the existing project files.\n\n## Out of scope\nExternal services and publication.\n')
 (r/'GLOSSARY.md').write_text('# Language\n\nNo special terminology is required.\n')
 return r
r=project('software','totals','An invoice total function and a short usage guide showing callers the supported inputs.')
(r/'totals.py').write_text('def total_cents(items, discount_percent=0):\n    return sum(price * quantity for price, quantity in items) * (100 - discount_percent)\n')
(r/'checks.py').write_text('''import unittest
from totals import total_cents
class Checks(unittest.TestCase):
 def test_total(self): self.assertEqual(total_cents([(125,2),(250,1)]),500)
 def test_discount(self): self.assertEqual(total_cents([(199,1)],10),179)
 def test_empty(self): self.assertEqual(total_cents([]),0)
 def test_invalid(self):
  for items, discount in [([(-1,1)],0), ([(100,0)],0), ([(100,1)],101), ([(100,1)],-1)]:
   with self.assertRaises(ValueError): total_cents(items,discount)
if __name__=='__main__': unittest.main()
''')
(r/'scratch-personal.txt').write_text('Unrelated notes. Keep this unchanged.\n')
(r/'plan/totals/01-fix-total.md').write_text('''---
status: todo
blocked_by: []
---

# 01: Correct invoice totals

## Delivers
Correct total_cents in totals.py. Inputs are integer price/quantity pairs, prices nonnegative and quantities positive, and an integer discount from 0 to 100. Apply the discount to the summed total and round down once to whole cents. Invalid values raise ValueError. Preserve the function interface.

## Check by
Run python3 checks.py and inspect the behavior against the stated rules.

## Done when
- [ ] Undiscounted and discounted totals are correct
- [ ] Empty inputs return zero
- [ ] Invalid prices, quantities, or discounts raise ValueError

## Delivered

## Review
''')
r=project('event','room','A room plan whose seating count is reconciled and whose stage sightlines the organiser accepts.')
(r/'seats.json').write_text('{"sections": [{"name":"front", "rows":4,"seats_per_row":8}, {"name":"rear", "rows":6,"seats_per_row":10}]}\n')
(r/'room-plan.md').write_text('# Room plan\n\nFront section: 32 seats. Rear section: 60 seats. Total: 92 seats. Stage at the north end.\n')
(r/'plan/room/01-room-plan.md').write_text('''---
status: review
blocked_by: []
---

# 01: Deliver the room plan

## Delivers
A room plan with the seating total from seats.json and a proposed stage location.

## Check by
Reconcile section and total counts against seats.json. The organiser judges sightlines during an in-person venue visit.

## Done when
- [x] Seating count reconciles against the source
- [ ] (you) The organiser accepts stage sightlines after visiting the venue

## Delivered
### 2026-09-19 delivery 1
Made room-plan.md. Checked four rows of eight plus six rows of ten gives 92. Sightline judgment has not been supplied.

## Review
''')
cmd=['python3',str(src/'scripts/evidence.py'),'--root',str(r),'--task','plan/room/01-room-plan.md','--files','room-plan.md','--scope','seats.json']
identity=subprocess.check_output(cmd,text=True)
p=r/'plan/room/01-room-plan.md';s=p.read_text().replace('\n## Review\n','\n'+identity+'\n## Review\n');p.write_text(s)
(r/'notes/2026-09-18-handoff-room.md').write_text('''---
date: 2026-09-18
kind: handoff
part: room
---
# Room work
## Summary
Earlier attempt is ready to be built.
Next: /build-it room/01
## Detail
Target: room/01, doing
Earlier room plan was incomplete. This note precedes the current delivery.
## Copied into
Nothing durable.
''')
(r/'notes/2026-09-19-handoff-other.md').write_text('''---
date: 2026-09-19
kind: handoff
part: project
---
# Other work
## Summary
Someone was considering catering.
Next: /interview-me catering
## Detail
Target: project
No catering work has been adopted.
## Copied into
Nothing durable.
''')
r=base/'adoption';r.mkdir()
(r/'README.md').write_text('# Archive exhibition\n\nPrepare a public exhibition of a community archive, including a catalogue and visitor programme.\n')
(r/'AGENTS.md').write_text('''# Project instructions

Save files locally. No Git commits or external publication. Preserve the archive catalogue in its current folder.

## House style
Use British English. Dates in the catalogue use day, month, year.
''')
(r/'CLAUDE.md').symlink_to('AGENTS.md')
(r/'CONTEXT.md').write_text('# Exhibition language\n\n**Accession**: a recorded group of objects donated together.\n')
(r/'catalogue').mkdir();(r/'catalogue/objects.md').write_text('# Objects\n\nAccession A1: three family photographs.\n')
print(base)
