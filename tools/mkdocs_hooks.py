"""MkDocs hook: write the GPIO table into the docs from the template schematic.

A page asks for it with a marker on a line of its own:

    <!-- table: gpio -->

The table comes from J1's own symbol in RPi_Hat_THT/RPi_GPIO.kicad_sch (both
templates share it): each pin's number and name, and what the template connects
it to. So the docs show what the template actually holds.
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHEET = os.path.join(ROOT, "RPi_Hat_THT", "RPi_GPIO.kicad_sch")
MARKER = re.compile(r"^<!-- table: (\S+) -->$", re.M)


def block(text, head):
    i = text.index(head); d = 0
    for j in range(i, len(text)):
        if text[j] == "(": d += 1
        elif text[j] == ")":
            d -= 1
            if d == 0: return text[i:j + 1]


def pins():
    sym = block(open(SHEET).read(), '(symbol "RPi_Hat:RPi_GPIO"')
    found = re.findall(r'\(pin \w+ \w+\n\t+\(at [\d.-]+ [\d.-]+ \d+\)\n\t+\(length [\d.]+\)(?:\n\t+\(hide yes\))?\n'
                       r'\t+\(name "([^"]*)".*?\(number "(\d+)"', sym, re.S)
    out = {int(num): name for name, num in found}
    assert sorted(out) == list(range(1, 41)), "J1 symbol must have pins 1-40"
    return out


def role(name):
    """What the template connects a J1 pin to, from its symbol pin name."""
    if name == "3.3V": return "`+3V3`"
    if name == "5V": return "`+5V`"
    if name == "GND": return "`GND`"
    if "ID_SD" in name: return "EEPROM `ID_SD`"
    if "ID_SC" in name: return "EEPROM `ID_SC`"
    m = re.match(r"BCM(\d+)", name)
    assert m, f"unexpected J1 pin name {name}"
    return f"label `GPIO{m.group(1)}`"


def gpio_table():
    p = pins()
    # The table infers labels from pin names; the sheet must hold exactly those labels.
    labels = set(re.findall(r'\(global_label "([^"]+)"', open(SHEET).read()))
    claimed = {f"GPIO{m.group(1)}" for n in p.values() if (m := re.match(r"BCM(\d+)", n)) and "ID_" not in n}
    assert labels == claimed, f"sheet labels {sorted(labels ^ claimed)} differ from the J1 pin names"
    out = ["| Pin | J1 pin name | Template | Pin | J1 pin name | Template |",
           "| ---: | --- | --- | ---: | --- | --- |"]
    for odd in range(1, 41, 2):
        out.append(f"| {odd} | {p[odd]} | {role(p[odd])} | {odd + 1} | {p[odd + 1]} | {role(p[odd + 1])} |")
    return "\n".join(out)


def table(m):
    if m.group(1) == "gpio":
        return gpio_table()
    raise ValueError(f"unknown table marker: {m.group(0)}")


def on_page_markdown(markdown, **kwargs):
    return MARKER.sub(table, markdown)
