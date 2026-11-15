# Mechanical

The outline and holes follow Raspberry Pi's
[HAT board mechanical drawing](https://github.com/raspberrypi/hats/blob/master/hat-board-mechanical.pdf);
its dimensions are on each template's `Dwgs.User` layer. The HAT+
specification is less strict about size than the original HAT specification:
it asks only for at least one mounting hole aligned with the Pi's, so you can
change the outline if your board needs to.

| Feature | From the drawing |
| --- | --- |
| Board | 65 × 56.5 mm with an SMT-style GPIO header, 65 × 56 mm with a through-hole one |
| Corners | 3 mm radius |
| Mounting holes | Four, M2.5, drilled 2.75 ± 0.05 mm, 58 mm apart along the header and 49 mm across |
| Hole land | At least 6.2 mm, isolated copper or bare board with open mask; ideally non-plated, never connected to GND |
| Camera flex slot | 2 × 17 mm |
| Display flex cut-out | 17 mm |

The templates' holes are non-plated, and their pads keep all copper 1.725 mm
from the hole edge, with the mask opened as far: a 6.2 mm bare land, which the
`B.Cu` GND pour respects.

## The flex slot and cut-out

The drawing recommends them so a camera and display can still be connected
with the HAT fitted; they are not required. Delete either from `Edge.Cuts` if
your board needs the space, and say in your documentation that the board
blocks that connector.

## Stack height

The HAT+ specification recommends at least 15 mm between the Pi and the HAT,
16 mm ideally, for the Raspberry Pi 5 Active Cooler, and more if the HAT has
parts on its underside. What height you can reach depends on the template:
see [Templates](templates.md#stack-height-decides-the-choice).
