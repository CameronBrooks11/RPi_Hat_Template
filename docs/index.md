# rpi-hat-kicad

KiCad 10 project templates for a Raspberry Pi
[HAT+](https://datasheets.raspberrypi.com/hat/hat-plus-specification.pdf): the
board outline, mounting holes, 40-pin GPIO connector and the ID EEPROM a HAT+
needs, placed, routed and passing DRC, ready to design on.

![Through-hole template, top view](renders/THT_top.png){ width="49%" }
![SMD template, top view](renders/SMD_top.png){ width="49%" }

## What you get

| | |
| --- | --- |
| [**Two templates**](templates.md) | One with a through-hole 2×20 GPIO socket, one with a Samtec surface-mount pass-through socket. |
| [**The ID EEPROM**](eeprom.md) | A CAT24C32 at address 0x50 with its pull-ups, decoupling, write-protect test point and write-enable jumper, as the HAT+ specification asks. |
| [**Every GPIO pin labelled**](pinout.md) | A global label on each free pin, `GPIO2` to `GPIO27`: place the same label in any sheet to use the pin. |
| **Checked boards** | Both templates pass DRC with schematic parity; ERC lists only the 26 GPIO labels you have not used yet. CI re-checks this on every change. |

## Start here

- **New HAT?** [Create a project from a template](getting-started.md).
- **Which template?** [Through-hole or SMD](templates.md): it decides how
  high your board sits above the Pi.
- **Calling it a HAT+?** The [HAT+ checklist](hat-plus.md) says what the
  template covers and what is still yours to do.

## Credit and licence

Derived from [RPi_Hat_Template](https://github.com/devbisme/RPi_Hat_Template)
by Dave Vandenbout, which laid both connectors and both outlines over each
other for the user to delete one. The GPIO symbol and the socket and header
footprints come from his [RPi_Hat.pretty](https://github.com/devbisme/RPi_Hat.pretty).

MIT licence; see
[LICENSE](https://github.com/CameronBrooks11/rpi-hat-kicad/blob/main/LICENSE).
Raspberry Pi is a trademark of Raspberry Pi Ltd; this project is not affiliated
with it.
