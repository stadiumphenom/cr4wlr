import os
import re

TESTS_DIR = "tests"

def fix_imports_in_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(r"\bfrom\s+krauler(\.[\w\.]*)?\s+import", r"from krauler\1 import", content)
    new_content = re.sub(r"\bimport\s+krauler\b", r"import krauler", new_content)

    if new_content != content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"✅ Fixed imports in {path}")

def walk_tests():
    for dirpath, _, filenames in os.walk(TESTS_DIR):
        for filename in filenames:
            if filename.endswith(".py"):
                fix_imports_in_file(os.path.join(dirpath, filename))

if __name__ == "__main__":
    if not os.path.exists(TESTS_DIR):
        print("❌ No tests/ folder found.")
    else:
        walk_tests()
        print("🎉 All test imports fixed.")
