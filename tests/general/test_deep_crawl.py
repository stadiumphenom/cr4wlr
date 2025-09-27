import asyncio
import time


from cr4wlr import CrawlerRunConfig, AsyncWebCrawler, CacheMode
from cr4wlr.content_scraping_strategy import LXMLWebScrapingStrategy
from cr4wlr.deep_crawling import BFSDeepCrawlStrategy
# from cr4wlr.deep_crawling import BFSDeepCrawlStrategy, BestFirstCrawlingStrategy


async def main():
    """Example deep crawl of documentation site."""
    config = CrawlerRunConfig(
        deep_crawl_strategy = BFSDeepCrawlStrategy(
            max_depth=2,
            include_external=False
        ),
        stream=False,
        verbose=True,
        cache_mode=CacheMode.BYPASS,
        scraping_strategy=LXMLWebScrapingStrategy()
    )

    async with AsyncWebCrawler() as crawler:
        start_time = time.perf_counter()
        print("\nStarting deep crawl in batch mode:")
        results = await crawler.arun(
            url="https://docs.cr4wlr.com",
            config=config
        )
        print(f"Crawled {len(results)} pages")
        print(f"Example page: {results[0].url}")
        print(f"Duration: {time.perf_counter() - start_time:.2f} seconds\n")

        print("Starting deep crawl in streaming mode:")
        config.stream = True
        start_time = time.perf_counter()
        async for result in await crawler.arun(
            url="https://docs.cr4wlr.com",
            config=config
        ):
            print(f"→ {result.url} (Depth: {result.metadata.get('depth', 0)})")
        print(f"Duration: {time.perf_counter() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())