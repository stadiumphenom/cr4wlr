import os
import re
import shutil

OLD = "cr4wlr"
NEW = "cr4wlr"
ROOT = "."  # path to your repo root

# File extensions to scan for imports / mentions
TEXT_EXTS = {".py", ".toml", ".md", ".txt", ".yml", ".yaml"}

def replace_in_file(path):
    """Replace OLD with NEW in a single file if extension matches."""
    _, ext = os.path.splitext(path)
    if ext.lower() not in TEXT_EXTS:
        return
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    if OLD not in text:
        return
    new_text = re.sub(rf"\b{OLD}\b", NEW, text)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print(f"Updated: {path}")

def walk_and_replace(root):
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            replace_in_file(path)

def rename_package_folder(root):
    old_path = os.path.join(root, OLD)
    new_path = os.path.join(root, NEW)
    if os.path.isdir(old_path):
        shutil.move(old_path, new_path)
        print(f"Renamed folder: {old_path} → {new_path}")

if __name__ == "__main__":
    walk_and_replace(ROOT)
    rename_package_folder(ROOT)
    print("✅ All done. Search & replace complete.")
