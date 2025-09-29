import traceback
import streamlit as st
import sys
import difflib
import os
from datetime import datetime

st.set_page_config(page_title="krauler UI", layout="wide")

error_count = st.session_state.get('error_count', 0)

try:
    st.title("🕷️ krauler: Streamlit Web Crawler UI")
    # Sidebar config
    with st.sidebar:
        st.header("Crawl Config")
        url = st.text_input("Target URL", "https://www.example.com")
        max_pages = st.number_input("Max Pages", min_value=1, max_value=1000, value=10)
        crawl_depth = st.number_input("Crawl Depth", min_value=1, max_value=100, value=3)
        run_btn = st.button("Run Crawl")

    result_box = st.empty()

    if run_btn:
        # Simulate live crawl results
        import time
        for i in range(1, max_pages+1):
            result_box.info(f"Crawling page {i}/{max_pages} (depth {crawl_depth})...")
            time.sleep(0.1)
        result_box.success(f"Crawl complete! {max_pages} pages crawled at depth {crawl_depth}.")

    # Copilot Testbench UI
    st.subheader("🤖 Copilot Testbench")
    code_input = st.text_area("Paste traceback or buggy code here:")
    if st.button("Ask Copilot for a fix") and code_input:
        # Simulate Copilot fix (replace 'raise' with 'pass' for demo)
        fixed_code = code_input.replace('raise', 'pass')
        diff = difflib.unified_diff(
            code_input.splitlines(),
            fixed_code.splitlines(),
            fromfile='original',
            tofile='fixed',
            lineterm=''
        )
        st.subheader("Preview Diff")
        st.code('\n'.join(diff), language="diff")
        if st.button("Approve and Apply Fix"):
            # Save backup
            with open("copilot_testbench_input.bak", "w") as f:
                f.write(code_input)
            # Overwrite with fix
            with open("copilot_testbench_input.py", "w") as f:
                f.write(fixed_code)
            st.success("Fix applied and backup saved.")

except Exception as e:
    error_msg = traceback.format_exc()
    st.sidebar.error("⚠️ Error caught: Check terminal or sidebar log.")
    st.sidebar.code(error_msg, language="python")
    print("\n\033[91m🚨 Streamlit UI Error:\033[0m\n" + error_msg, file=sys.stderr)
    # Save backup before overwrite
    if os.path.exists(__file__):
        with open(__file__ + ".bak", "w") as f:
            with open(__file__, "r") as orig:
                f.write(orig.read())
    with open("last_error.txt", "w") as f:
        f.write(error_msg)
    error_count += 1
    st.session_state['error_count'] = error_count
    if error_count >= 3:
        st.warning("Error persisted 3 times. Would open GitHub issue.")
        st.write(f"[Auto] Streamlit Crash Report\nTime: {datetime.now()}\nCommit: (simulated)\nError:\n{error_msg}")

# Copilot: use the last_error.txt to suggest a fix or auto-modify this file
