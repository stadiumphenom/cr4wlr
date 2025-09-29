import streamlit as st
import asyncio
import pandas as pd
from krauler.core.crawler import start_crawl
from krauler.utils.storage import load_results_as_df

st.set_page_config(page_title="🕷️ Krauler", layout="wide")
st.title("🕷️ Krauler: AI-Ready Web Crawler")

with st.form("crawl_form"):
    seed_url = st.text_input("🔗 Seed URL", placeholder="https://example.com")
    keyword_filter = st.text_input("🧠 Keyword Filter (optional)")
    crawl_depth = st.slider("📐 Max Crawl Depth", 1, 5, 2)
    submit = st.form_submit_button("🚀 Start Crawl")

if submit and seed_url:
    st.info(f"Starting crawl at: {seed_url}...")
    with st.spinner("Crawling in progress..."):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(
            start_crawl(seed_url=seed_url, max_depth=crawl_depth, keyword=keyword_filter or None)
        )
    st.success("✅ Crawl completed!")
    df = load_results_as_df()
    if not df.empty:
        st.subheader("📊 Crawl Results Preview")
        st.dataframe(df)
        st.download_button("⬇️ Download JSON", df.to_json(orient="records"), file_name="crawl_results.json")
        st.download_button("⬇️ Download CSV", df.to_csv(index=False), file_name="crawl_results.csv")
    else:
        st.warning("No crawl results found.")
