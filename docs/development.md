# Development

Work on the templates themselves, rather than a project made from one.

You need [just](https://just.systems/), Python 3 and KiCad 10's `kicad-cli`;
the docs also need [uv](https://docs.astral.sh/uv/).

## Layout

| Path | What it holds |
| --- | --- |
| `RPi_Hat_THT/`, `RPi_Hat_SMD/` | The two templates: project, schematic (`RPi_GPIO.kicad_sch` holds J1 and the EEPROM), board, design rules, their own `RPi_Hat` libraries, and `meta/` for KiCad's template chooser |
| `tools/` | `expect_erc.py`, used by `just check`; `mkdocs_hooks.py`, which writes the GPIO table into this site |
| `docs/` | This site |

## Recipes

| Recipe | What it does |
| --- | --- |
| `just check` | The gate; see below. CI runs it in the `kicad/kicad:10.0.6` image on every pull request and push to `main`. |
| `just renders` | Renders the pictures for this site into `docs/renders/`. |
| `just docs` | Builds this site into `site/`, failing on any warning. |
| `just serve` | Serves this site at <http://127.0.0.1:8000> while you edit. |

`just check` fails unless:

- the two templates' `RPi_Hat` libraries are identical;
- each template's ERC finds exactly 26 `isolated_pin_label` warnings and
  nothing else;
- each template's DRC, with schematic parity and zones refilled, finds 0
  violations and 0 unconnected items.

## Changing a template

Edit it in KiCad, then:

- make the same change in the other template where it applies;
- copy any library change across, so the two `RPi_Hat` copies stay identical;
- refill zones, and run DRC with parity;
- regenerate `meta/brd.png` if the board changed (`kicad-cli pcb render
  --side top --width 1288 --height 1120 --background transparent`);
- update the counts in `just check` if a change is meant to alter them.

## These docs

The site is [MkDocs](https://www.mkdocs.org/) with the
[Material](https://squidfunk.github.io/mkdocs-material/) theme. The GPIO
table is written at build time from the THT template's schematic by
`tools/mkdocs_hooks.py`, which fails the build if the sheet's labels and J1's
pin names disagree. CI builds the site on every pull request and publishes it
from `main`.

```sh
just renders
just serve
```
