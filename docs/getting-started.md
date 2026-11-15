# Getting started

Everything here needs KiCad 10. CI checks the templates with KiCad 10.0.6.

## Create a project

1. Clone the repository, or download it as a zip from
   [GitHub](https://github.com/CameronBrooks11/rpi-hat-kicad) and unzip it.
2. In KiCad choose **File → New Project from Template**, open the user
   templates tab and point it at the folder that holds `RPi_Hat_THT` and
   `RPi_Hat_SMD`. To list them every time, set `KICAD_USER_TEMPLATE_DIR` to
   that folder under **Preferences → Configure Paths**.
3. Pick a template ([which one](templates.md)) and name the project. KiCad
   copies the files and renames them after the project, including the design
   rules file (`<project>.kicad_dru`) that each template needs to pass DRC.

The new project opens without installing anything: every part it uses is in
its own `RPi_Hat` symbol and footprint libraries.

## What a fresh project reports

| Check | Result |
| --- | --- |
| ERC | 26 warnings, `isolated_pin_label`, one per GPIO label you have not used yet; no errors |
| DRC, with schematic parity and zones refilled | 0 violations, 0 unconnected items, 0 parity issues |

The ERC warnings are the to-do list: each one disappears when you use its pin.
The ones left at the end are the pins your design leaves free.

## Design your HAT

1. **Use GPIO pins by label.** Place a global label named for the pin, such as
   `GPIO17`, on the part that connects to it, in any sheet. You never need to
   edit the J1 sheet. [GPIO pinout](pinout.md) lists every label.
2. **Leave ID_SD and ID_SC alone.** They belong to the ID EEPROM, and the
   specification allows nothing else on them.
3. **Delete the camera flex slot** from `Edge.Cuts` if your board does not
   need it. The display cut-out can go too. Both are recommended, not
   required; see [Mechanical](mechanical.md).
4. **Mind the rest of the [HAT+ checklist](hat-plus.md)**, in particular the
   power-on state and the stack height.
5. **Program the EEPROM** once the board exists: [ID EEPROM](eeprom.md).

## Not making a HAT+?

Delete U1, R1 to R3, C1, TP1 and JP1, and leave ID_SD and ID_SC unconnected.
The board is then an add-on board rather than a HAT+, which the specification
allows; it just cannot use the HAT+ name.
