import asyncio
import time


from krauler import CrawlerRunConfig, AsyncWebCrawler, CacheMode
from krauler.content_scraping_strategy import LXMLWebScrapingStrategy
from krauler.deep_crawling import BFSDeepCrawlStrategy, BestFirstCrawlingStrategy
from krauler.deep_crawling.filters import FilterChain, URLPatternFilter, DomainFilter, ContentTypeFilter, ContentRelevanceFilter
from krauler.deep_crawling.scorers import KeywordRelevanceScorer
# from krauler.deep_crawling import BFSDeepCrawlStrategy, BestFirstCrawlingStrategy


async def main():
    """Example deep crawl of documentation site."""
    filter_chain = FilterChain([
        URLPatternFilter(patterns=["*2025*"]),
        DomainFilter(allowed_domains=["techcrunch.com"]),
        ContentRelevanceFilter(query="Use of artificial intelligence in Defence applications", threshold=1),
        ContentTypeFilter(allowed_types=["text/html","application/javascript"])
    ])
    config = CrawlerRunConfig(
        deep_crawl_strategy = BestFirstCrawlingStrategy(
            max_depth=2,
            include_external=False,
            filter_chain=filter_chain,
            url_scorer=KeywordRelevanceScorer(keywords=["anduril", "defence", "AI"]),
        ),
        stream=False,
        verbose=True,
        cache_mode=CacheMode.BYPASS,
        scraping_strategy=LXMLWebScrapingStrategy()
    )

    async with AsyncWebCrawler() as crawler:
        print("Starting deep crawl in streaming mode:")
        config.stream = True
        start_time = time.perf_counter()
        async for result in await crawler.arun(
            url="https://techcrunch.com",
            config=config
        ):
            print(f"→ {result.url} (Depth: {result.metadata.get('depth', 0)})")
        print(f"Duration: {time.perf_counter() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())