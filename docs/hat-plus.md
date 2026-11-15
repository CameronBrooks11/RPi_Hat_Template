# HAT+ checklist

Raspberry Pi's
[HAT+ specification](https://datasheets.raspberrypi.com/hat/hat-plus-specification.pdf)
(release of 5 December 2024) replaces the original HAT specification, which it
marks deprecated. A board may be called a HAT+ only if it meets the
specification's minimum electrical and mechanical requirements. This page
lists them, and says which the templates meet for you and which are yours.

## Required

| Requirement (specification chapter) | Templates |
| --- | --- |
| Plugs into the 40-way GPIO header, including the ID pins (6, 7) | **Done.** J1 is the full 40-pin connector. |
| An ID EEPROM on ID_SD and ID_SC, with 3.9 kΩ pull-ups to 3.3 V, holding data to the HAT+ EEPROM format (3, 6) | **Circuit done**; [programming it](eeprom.md) is yours. |
| Nothing but the EEPROM and its pull-ups on ID_SD and ID_SC (2) | **Done**, and the schematic says so; keep it that way. |
| At least one mounting hole aligned with one of the Pi's four (7) | **Done.** All four are there. |
| If powered from the GPIO header, electrically compatible with the STANDBY state: 5 V present, 3.3 V off (1, 6) | **Yours.** Check every part on +5V for what it does while +3V3 is off, and anything that would back-feed +3V3. |
| Tolerates the weak pull-ups and pull-downs the Pi applies to every GPIO at power-on, in any order; provides its own pull where it needs a defined state (2.3) | **Yours.** GPIO2 and GPIO3 also carry about 2 kΩ pull-ups to 3.3 V on the Pi. |
| A Power HAT+ (one that powers the Pi) supplies at least 3 A at 5.1 V, 5 A recommended, and only sources current (4, 6) | **Yours**, if your board powers the Pi. It then also needs a Power class EEPROM address; see [address class](eeprom.md#address-class). |

## Recommended

| Recommendation (chapter 7) | Templates |
| --- | --- |
| Stays clear of the Pi 4 and Pi 5 PoE headers | **Yours** for parts and their leads; the templates put nothing in that area. |
| Spacers of at least 15 mm, 16 mm ideal, so a Pi 5 Active Cooler fits; more if the HAT has parts underneath | **Depends on the template**: possible with through-hole, not with the SMD socket. See [Templates](templates.md#stack-height-decides-the-choice). |
| Does not block access to the camera, display and PCIe flex connectors | **Done** for camera and display: the outline keeps the flex slot and cut-out. Keep them unless your board cannot. |

## Naming

A HAT+ should use "HAT+" in its name. One that works only with some Pi models
must say which, on the board and in its documentation; one that stacks with
another HAT must say so in its documentation (chapter 5).
