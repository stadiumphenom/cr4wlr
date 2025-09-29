#!/usr/bin/env python3
import os
import re
from pathlib import Path

test_dir = Path('tests')
pattern = re.compile(r'from\s+krauler(\.[\w_]+)?\s+import')

for root, dirs, files in os.walk(test_dir):
    for file in files:
        if file.endswith('.py'):
            path = Path(root) / file
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                new_content = re.sub(r'from\s+krauler(\.[\w_]+)?\s+import',
                                    lambda m: f"from krauler{m.group(1) or ''} import", content)
                if new_content != content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated imports in {path}")
            except Exception:
                continue
