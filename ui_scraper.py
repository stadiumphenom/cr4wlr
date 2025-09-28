import streamlit as st
import asyncio
from cr4wlr import WebCrawler

st.set_page_config(page_title="cr4wlr Scraper", layout="wide")

st.title("🕸️ cr4wlr Web Scraper")

url = st.text_input("Enter URL to scrape:", "https://quotes.toscrape.com/")
selector = st.text_input("CSS Selector (optional):", ".quote")
run_btn = st.button("Run Scrape")

if run_btn and url:
    with st.spinner("Scraping in progress..."):
        async def scrape():
            crawler = WebCrawler()
            result = await crawler.crawl(url)
            if selector:
                items = [el.get_text() for el in result.soup.select(selector)]
                return {"title": result.title, "items": items}
            else:
                return {"title": result.title, "html": result.html[:2000]}  # limit output

        output = asyncio.run(scrape())

    st.subheader("✅ Scrape Result")
    st.json(output)
