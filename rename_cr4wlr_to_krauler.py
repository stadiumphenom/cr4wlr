#!/usr/bin/env python3
import os
import sys
import argparse
import shutil
import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.resolve()
TARGET_NAME = "krauler"
OLD_NAME = "krauler"
FILE_EXTS = {".py", ".toml", ".md", ".yml", ".yaml", ".txt"}

summary = {
    "text_replacements": [],
    "renamed_files": [],
    "renamed_dirs": [],
    "pyproject_updated": False,
}

def should_edit_file(path):
    return path.suffix in FILE_EXTS

def replace_in_file(path, dry_run):
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if OLD_NAME in content:
            new_content = content.replace(OLD_NAME, TARGET_NAME)
            if not dry_run:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_content)
            summary["text_replacements"].append(str(path))
    except Exception as e:
        print(f"Error processing {path}: {e}")

def walk_and_replace(root, dry_run):
    for dirpath, dirnames, filenames in os.walk(root):
        # Replace in files
        for filename in filenames:
            path = Path(dirpath) / filename
            if should_edit_file(path):
                replace_in_file(path, dry_run)

def rename_dirs_and_files(root, dry_run):
    # First, rename directories (deepest first)
    for dirpath, dirnames, filenames in os.walk(root, topdown=False):
        for dirname in dirnames:
            if dirname == OLD_NAME:
                old_dir = Path(dirpath) / dirname
                new_dir = Path(dirpath) / TARGET_NAME
                if not dry_run:
                    shutil.move(str(old_dir), str(new_dir))
                summary["renamed_dirs"].append(f"{old_dir} -> {new_dir}")
        # Then, rename files
        for filename in filenames:
            if filename == OLD_NAME:
                old_file = Path(dirpath) / filename
                new_file = Path(dirpath) / TARGET_NAME
                if not dry_run:
                    shutil.move(str(old_file), str(new_file))
                summary["renamed_files"].append(f"{old_file} -> {new_file}")

def update_pyproject_toml(pyproject_path, dry_run):
    try:
        with open(pyproject_path, "r", encoding="utf-8") as f:
            content = f.read()
        updated = False
        # Update [project] name
        content, n1 = re.subn(r'(name\s*=\s*")krauler("\s*)', rf'\1{TARGET_NAME}\2', content)
        # Update setuptools include
        content, n2 = re.subn(r'(include\s*=\s*\[)[^\]]*\]', f'\1"{TARGET_NAME}*"]', content)
        if n1 or n2:
            updated = True
            if not dry_run:
                with open(pyproject_path, "w", encoding="utf-8") as f:
                    f.write(content)
        if updated:
            summary["pyproject_updated"] = True
    except Exception as e:
        print(f"Error updating pyproject.toml: {e}")

def print_summary():
    print("\nSummary of changes:")
    print(f"Text replacements in files: {len(summary['text_replacements'])}")
    for f in summary["text_replacements"]:
        print(f"  - {f}")
    print(f"Renamed directories: {len(summary['renamed_dirs'])}")
    for d in summary["renamed_dirs"]:
        print(f"  - {d}")
    print(f"Renamed files: {len(summary['renamed_files'])}")
    for f in summary["renamed_files"]:
        print(f"  - {f}")
    print(f"pyproject.toml updated: {summary['pyproject_updated']}")

def main():
    parser = argparse.ArgumentParser(description="Rename krauler package to krauler.")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without modifying files.")
    args = parser.parse_args()
    dry_run = args.dry_run

    walk_and_replace(REPO_ROOT, dry_run)
    rename_dirs_and_files(REPO_ROOT, dry_run)
    pyproject_path = REPO_ROOT / "pyproject.toml"
    if pyproject_path.exists():
        update_pyproject_toml(pyproject_path, dry_run)
    print_summary()
    if dry_run:
        print("\n(DRY RUN: No files were modified)")

if __name__ == "__main__":
    main()
