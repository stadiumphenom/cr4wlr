#!/usr/bin/env python3
import os
import sys
from pathlib import Path

EXCLUDE_DIRS = {'.git', '.venv', 'dist', 'build'}
MATCH = 'krauler'

found = False

for root, dirs, files in os.walk('.', topdown=True):
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
    for file in files:
        path = Path(root) / file
        try:
            with open(path, 'r', encoding='utf-8') as f:
                for i, line in enumerate(f, 1):
                    if MATCH in line:
                        print(f'{path}:{i}: {line.strip()}')
                        found = True
        except Exception:
            continue

sys.exit(1 if found else 0)
