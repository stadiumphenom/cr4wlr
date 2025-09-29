import os
import shutil
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(ROOT, "src")
PKG_DIR = os.path.join(SRC_DIR, "krauler")
PYPROJECT = os.path.join(ROOT, "pyproject.toml")

def ensure_dirs():
    os.makedirs(PKG_DIR, exist_ok=True)
    init_file = os.path.join(PKG_DIR, "__init__.py")
    if not os.path.exists(init_file):
        with open(init_file, "w", encoding="utf-8") as f:
            f.write("# krauler package\n")

def move_package_files():
    if os.path.exists(os.path.join(ROOT, "krauler")):
        for filename in os.listdir(os.path.join(ROOT, "krauler")):
            src_file = os.path.join(ROOT, "krauler", filename)
            dst_file = os.path.join(PKG_DIR, filename)
            if os.path.isfile(src_file):
                print(f"Moving {src_file} → {dst_file}")
                shutil.move(src_file, dst_file)
        # cleanup old folder if empty
        try:
            os.rmdir(os.path.join(ROOT, "krauler"))
        except OSError:
            pass

def patch_pyproject():
    if not os.path.exists(PYPROJECT):
        print("❌ pyproject.toml not found.")
        return

    with open(PYPROJECT, "r", encoding="utf-8") as f:
        content = f.read()

    setuptools_block = """
[tool.setuptools]
packages = {find = {where = ["src"], include = ["krauler*"]}}
package-dir = {"" = "src"}
"""

    if "[tool.setuptools]" not in content:
        content += "\n" + setuptools_block
    else:
        # Replace existing block if present
        content = re.sub(r"\[tool\.setuptools\][\s\S]*?(?=\n\[|$)", setuptools_block, content)

    with open(PYPROJECT, "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ Patched pyproject.toml for src layout")

if __name__ == "__main__":
    ensure_dirs()
    move_package_files()
    patch_pyproject()
    print("🎉 Restructure complete! Now run: pip install -e .[all]")
