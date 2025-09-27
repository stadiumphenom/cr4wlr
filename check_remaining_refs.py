import os

def scan_for_string(root, target):
    hits = []
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            # Only scan source/config/docs files
            if filename.endswith((".py", ".toml", ".md", ".txt", ".yml", ".json")):
                filepath = os.path.join(dirpath, filename)
                try:
                    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                        for i, line in enumerate(f, start=1):
                            if target in line:
                                hits.append((filepath, i, line.strip()))
                except Exception as e:
                    print(f"⚠️ Skipped {filepath}: {e}")
    return hits

if __name__ == "__main__":
    target = "crawl4ai"
    repo_root = "."
    results = scan_for_string(repo_root, target)

    if results:
        print(f"\n⚠️ Found {len(results)} remaining references to '{target}':\n")
        for filepath, line_no, snippet in results:
            print(f"{filepath}:{line_no} → {snippet}")
    else:
        print(f"\n✅ No references to '{target}' found. You're clean!\n")
