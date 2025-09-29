import asyncio
import json
from pathlib import Path

async def start_crawl(seed_url, max_depth=2, keyword=None):
    # Dummy async crawl logic for demo
    results = []
    for i in range(1, max_depth+1):
        results.append({
            "url": f"{seed_url}/page{i}",
            "depth": i,
            "keyword": keyword or "",
            "content": f"Sample content for {seed_url}/page{i}"
        })
        await asyncio.sleep(0.1)
    # Save results to output/data.jsonl
    out_path = Path("output/data.jsonl")
    out_path.parent.mkdir(exist_ok=True)
    with open(out_path, "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")
