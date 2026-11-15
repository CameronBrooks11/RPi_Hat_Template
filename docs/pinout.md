# GPIO pinout

What each of J1's 40 pins is, and what the template connects it to. This
table is written from the template's own schematic each time the site is
built.

<!-- table: gpio -->

The J1 pin names are BCM GPIO numbers with a common alternate function
(`BCM2_SDA`); which functions a pin actually has depends on the Device Tree
overlay your design uses. [pinout.xyz](https://pinout.xyz/) shows them all.

## Using a pin

Each free GPIO pin carries a **global label** named for its BCM number. To use
a pin, place a global label of the same name, such as `GPIO17`, on the part it
connects to, in any sheet. The J1 sheet itself never needs editing.

- A global label joins every label of that name in the design, so do not reuse
  `GPIO2` to `GPIO27` for anything else.
- Until a label is used elsewhere, ERC reports it as `isolated_pin_label`, a
  warning. Each warning disappears as its pin is used.
- Rename a label, if you prefer a functional name, on J1's sheet; keep the
  pin it sits on.

## Pins to know about

- **ID_SD and ID_SC** (pins 27 and 28) are the ID EEPROM's and nothing else's.
- **GPIO2 and GPIO3** (pins 3 and 5) have about 2 kΩ pull-ups to 3.3 V on the
  Pi itself, so they idle high.
- **GPIO6, GPIO14 and GPIO16** may be driven as outputs at boot by very old
  firmware that mistakes a newer Pi for a Model B. Raspberry Pi's
  [design guide](https://github.com/raspberrypi/hats/blob/master/designguide.md)
  asks boards that also drive these pins to protect against it, for example
  with a series resistor.
