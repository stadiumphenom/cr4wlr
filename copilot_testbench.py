import difflib
import streamlit as st
import os
import traceback
from datetime import datetime

st.set_page_config(page_title="Copilot Testbench", layout="wide")

st.title("🤖 Copilot Testbench")

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

# Error persistence logic (demo)
error_count = st.session_state.get('error_count', 0)
if os.path.exists("last_error.txt"):
    with open("last_error.txt") as f:
        last_error = f.read()
    st.text_area("Last Error", last_error)
    error_count += 1
    st.session_state['error_count'] = error_count
    if error_count >= 3:
        st.warning("Error persisted 3 times. Would open GitHub issue.")
        # Simulate GitHub issue creation
        st.write(f"[Auto] Streamlit Crash Report\nTime: {datetime.now()}\nCommit: (simulated)\nError:\n{last_error}")

# Copilot: use the last_error.txt to suggest a fix or auto-modify this file
