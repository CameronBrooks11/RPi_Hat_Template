# Templates

Both templates hold the same schematic, the same ID EEPROM and the same
board outline from Raspberry Pi's
[HAT mechanical drawing](https://github.com/raspberrypi/hats/blob/master/hat-board-mechanical.pdf).
They differ in the GPIO connector, J1, and that decides how the board meets
the Pi.

| | `RPi_Hat_THT` | `RPi_Hat_SMD` |
| --- | --- | --- |
| J1 | 2×20 through-hole, 2.54 mm pitch | Samtec HLE-120-02-xxx-DV-BE surface-mount socket |
| Mounted | A female socket on the **underside**, onto the Pi's pins | On the **top side**; the Pi's pins come up through the board into it |
| Board | 65 × 56 mm | 65 × 56.5 mm |
| Stack height | Set by the socket you fit: any 2×20 female header or stacking header | As low as the Pi's header allows (see below) |
| Extra design rule | One thermal spoke allowed on J1's GND pins | 0.127 mm pad-to-hole clearance allowed inside the socket |

The board sizes follow the drawing: 65 × 56.5 mm for an SMT-style GPIO
header, 65 × 56 mm for a through-hole one.

## Stack height decides the choice

The [HAT+ specification](https://datasheets.raspberrypi.com/hat/hat-plus-specification.pdf)
recommends spacers of at least 15 mm between the Pi and a HAT+, 16 mm ideally,
so a Raspberry Pi 5 Active Cooler fits underneath, and more if your HAT has
parts on its underside.

**Through-hole** meets that with the right part. The footprint is just the 40
holes, so fit whichever female header or stacking header gives the height you
need, with spacers of the same height.

**SMD** cannot be raised. Samtec's `-BE` option is *bottom entry*: the socket
sits on top of the HAT and the Pi's pins pass up through the board into it,
needing at least 2.59 mm of insertion
([HLE datasheet](https://suddendocs.samtec.com/catalog_english/hle.pdf)). The
HAT therefore sits about as low as the Pi's own header body, well under 15 mm.
Use it for a low-profile HAT on a Pi with nothing tall under the HAT area, not
on a Pi 5 with an Active Cooler.

![Through-hole template from below, with its socket](renders/THT_bottom.png){ width="60%" }

## What both templates hold

- The outline with the display flex cut-out and the camera flex slot, the
  drawing's dimensions on `Dwgs.User`, and four M2.5 mounting holes. See
  [Mechanical](mechanical.md).
- J1, placed and locked at the drawing's position.
- The schematic: J1's power pins wired, a global label on each GPIO pin, and
  the ID EEPROM. See the [GPIO pinout](pinout.md) and [ID EEPROM](eeprom.md).
- The board: the EEPROM block routed, a GND pour on `B.Cu`. See
  [Board design](board.md).
- Their own `RPi_Hat` libraries; the two copies are identical, and CI checks
  that they stay so.

## Where they live

`RPi_Hat_THT/` and `RPi_Hat_SMD/` in the
[repository](https://github.com/CameronBrooks11/rpi-hat-kicad). Each folder's
`meta/` holds what KiCad shows in its template chooser.
