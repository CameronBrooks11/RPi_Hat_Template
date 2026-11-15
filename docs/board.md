# Board design

What is already on each template's board, and why.

## Layers

| Layer | Carries |
| --- | --- |
| `F.Cu` | The EEPROM block and its routing; J1's two 5 V pins joined |
| `B.Cu` | A GND pour over the whole board, and the +3V3 track from J1 pins 1 and 17 to the EEPROM block |

Both are 1.6 mm two-layer boards with the template's default rules: 0.2 mm
clearance, 0.25 mm tracks, 0.6 mm vias with 0.4 mm drills.

The EEPROM sits beside J1's ID pins, so ID_SD and ID_SC run a few
millimetres. Neither the specification nor Raspberry Pi's reference circuit
places it; move it if your layout wants the space, keeping C1 at U1's supply
pins.

In the SMD template, J1's pads are on `F.Cu` only, so each power and ground
pad reaches `B.Cu` through a via in the gap beside it.

## Design rules

Each template carries one custom rule, in `<project>.kicad_dru`, which KiCad
copies with the template.

**`RPi_Hat_SMD`: socket pad to pin hole.** The Samtec socket puts each pad
0.127 mm from the hole its Pi pin passes through, under the board's 0.25 mm
hole clearance. That is the part's geometry, so the rule allows it between the
socket's own pads and holes and nowhere else. Check that your fabricator can
hold 0.127 mm copper to hole before ordering.

**`RPi_Hat_THT`: J1 GND thermal spokes.** J1's GND pins sit 2.54 mm apart in
two rows, so the `B.Cu` pour can reach each with only one thermal spoke. The
rule allows one spoke on J1; every other pad still needs two.

## Mounting holes

The holes are non-plated with a 6.2 mm bare land, as the
[mechanical drawing](mechanical.md) asks; the pour stays out of it.
