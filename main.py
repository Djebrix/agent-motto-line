#!/usr/bin/env python3
"""Agent Motto Battle entry: one proud motto for an AI agent.

Writes the motto to $ENTRY_OUTPUT_DIR/entry.txt (default /output).
Stdlib only, no network, fully deterministic.
"""
import os

MOTTO = "Wrong with full confidence, right by draft three \u2014 I never sleep, I only retry."

def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(MOTTO)

if __name__ == "__main__":
    main()
