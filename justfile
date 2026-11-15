templates := "RPi_Hat_THT RPi_Hat_SMD"

default:
    @just --list

# Library copies, ERC (only the 26 GPIO label warnings) and DRC with parity on both templates
check:
    #!/usr/bin/env bash
    set -uo pipefail
    tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
    fail() { echo "FAIL: $1"; [ -n "${2:-}" ] && cat "$2"; exit 1; }
    cmp -s RPi_Hat_THT/RPi_Hat.kicad_sym RPi_Hat_SMD/RPi_Hat.kicad_sym && diff -r RPi_Hat_THT/RPi_Hat.pretty RPi_Hat_SMD/RPi_Hat.pretty >/dev/null \
      || fail "the two templates' RPi_Hat libraries differ"
    echo "RPi_Hat library: identical in both templates"
    for t in {{templates}}; do
      # A fresh project's only ERC findings are the warnings for the 26 GPIO labels it has not used yet
      kicad-cli sch erc --severity-all --format json -o "$tmp/erc.json" "$t/$t.kicad_sch" >/dev/null
      python3 tools/expect_erc.py "$tmp/erc.json" isolated_pin_label=26 || fail "$t: ERC" "$tmp/erc.json"
      echo "$t: ERC finds only the 26 GPIO label warnings"
      kicad-cli pcb drc --severity-all --schematic-parity --refill-zones --exit-code-violations -o "$tmp/drc.rpt" "$t/$t.kicad_pcb" >/dev/null \
        || fail "$t: DRC" "$tmp/drc.rpt"
      echo "$t: DRC clean, schematic parity clean"
    done

# Render the docs' pictures with kicad-cli into docs/renders/: both boards and the GPIO sheet
renders:
    #!/usr/bin/env bash
    set -euo pipefail
    out=docs/renders; rm -rf "$out"; mkdir -p "$out"
    render() { kicad-cli pcb render --side "$2" --width 1400 --height 1200 --quality basic --background opaque -o "$out/$3.png" "$1" >/dev/null; }
    render RPi_Hat_THT/RPi_Hat_THT.kicad_pcb top THT_top
    render RPi_Hat_THT/RPi_Hat_THT.kicad_pcb bottom THT_bottom
    render RPi_Hat_SMD/RPi_Hat_SMD.kicad_pcb top SMD_top
    kicad-cli sch export svg -o "$out/sch" RPi_Hat_THT/RPi_Hat_THT.kicad_sch >/dev/null
    mv "$out/sch/RPi_Hat_THT-RPi_GPIO.svg" "$out/gpio_sheet.svg"; rm -r "$out/sch"
    ls "$out"

# Build the docs site into site/ (after just renders), failing on any warning
docs:
    uv run --no-project --with-requirements docs/requirements.txt mkdocs build --strict

# Serve the docs site at http://127.0.0.1:8000 while editing
serve:
    uv run --no-project --with-requirements docs/requirements.txt mkdocs serve
