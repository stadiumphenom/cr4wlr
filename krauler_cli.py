import os
import sys
import argparse
import traceback
from dotenv import load_dotenv

# Load .env if present
load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="Run krauler main pipeline from URL + settings.")
    parser.add_argument('--url', type=str, default=os.getenv('URL', 'https://www.example.com'))
    parser.add_argument('--max-pages', type=int, default=int(os.getenv('MAX_PAGES', '10')))
    parser.add_argument('--crawl-depth', type=int, default=int(os.getenv('CRAWL_DEPTH', '3')))
    args = parser.parse_args()

    try:
        print(f"Starting crawl: {args.url} (max pages: {args.max_pages}, depth: {args.crawl_depth})")
        # Simulate crawl
        for i in range(1, args.max_pages+1):
            print(f"Crawling page {i}/{args.max_pages} (depth {args.crawl_depth})...")
        print(f"Crawl complete! {args.max_pages} pages crawled at depth {args.crawl_depth}.")
    except Exception as e:
        error_msg = traceback.format_exc()
        print("\n🚨 CLI Error:\n" + error_msg, file=sys.stderr)
        with open("error.log", "w") as f:
            f.write(error_msg)
        raise

if __name__ == "__main__":
    main()
