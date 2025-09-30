🕷️ Krauler

Clean, AI-ready web crawler for invention pipelines, research, and data mining.

Krauler is a lightweight, async-first web crawling framework with a Streamlit-powered UI, LLM-ready outputs, and self-healing diagnostics. It’s built for researchers, inventors, and builders who want to gather structured data fast — without wrestling with bloated scraping frameworks.

✨ Features

🚀 Async-first engine → powered by aiohttp, playwright, and stealth browsing

🧠 LLM-ready outputs → crawl data structured for AI/ML pipelines (JSONL, CSV)

🖼 Streamlit dashboard → no CLI required; paste URLs, run crawls, see results

🔍 Flexible extraction → text, metadata, links, images

🔄 Self-healing diagnostics → detects broken imports, pyproject issues, missing deps

⚡ Extensible → plug in rankers (BM25, embeddings), custom agents, or export pipelines

🛠 Developer-friendly → simple config, modular design, ready for CI/CD

📦 Installation
# clone your fork
git clone https://github.com/your-username/krauler.git
cd krauler

# install in editable mode
pip install -e .[all]

# install playwright browsers
playwright install

🖥️ Usage
🔹 Command Line
# run a basic crawl
python -m krauler.cli https://example.com --depth 2 --text

🔹 Streamlit App
streamlit run ui/app.py --server.port 8501


Then open http://localhost:8501
 in your browser.
From there, you can:

Paste one or more URLs

Set crawl depth

Select extraction mode (text, images, metadata)

View live results

Export to JSON or CSV

🧭 Project Structure
krauler/
├── src/krauler/         # core package
│   ├── core/            # crawler engine
│   ├── parsers/         # HTML/data parsers
│   ├── storage/         # async storage (sqlite/jsonl)
│   ├── ui/              # Streamlit app
│   └── __init__.py
├── ui/app.py            # main Streamlit dashboard
├── tests/               # pytest suite
├── pyproject.toml       # project config
└── README.md

🧪 Development
Run tests
pytest

Lint + type check
ruff check .
mypy src/krauler

Build package
python -m build

🚦 CI/CD

✅ PRs → Publish to TestPyPI

✅ Tags (vX.Y.Z) → Publish to PyPI

✅ Docker image auto-builds at ghcr.io/<owner>/krauler:latest

🧠 Why Krauler?

Unlike heavyweights like Scrapy, Krauler is:

Lightweight (no spiders/config bloat)

Async-native (no thread hell)

LLM-focused (outputs structured chunks for embedding/training)

UI-first (Streamlit dashboard = no barrier to entry)

It’s not just a crawler — it’s a data-gathering workbench for the AI era.

📜 License

Apache 2.0 — free to use, modify, and share.

🤝 Contributing

Contributions welcome!

Fork the repo

Create a feature branch

Submit a PR

⭐ Acknowledgements

Built with inspiration from:

Playwright

BeautifulSoup

Streamlit

litellm

🔥 Ready to crawl the web smarter? Start with:

streamlit run ui/app.py
