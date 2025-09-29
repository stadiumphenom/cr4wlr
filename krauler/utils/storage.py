import pandas as pd
from pathlib import Path
import json

def load_results_as_df():
    out_path = Path("output/data.jsonl")
    if not out_path.exists():
        return pd.DataFrame()
    with open(out_path) as f:
        lines = [json.loads(line) for line in f if line.strip()]
    return pd.DataFrame(lines)
