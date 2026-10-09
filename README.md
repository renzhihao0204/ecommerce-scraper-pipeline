# 📦 E-Commerce Scraper & Clean Data Pipeline

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Async](https://img.shields.io/badge/Async-httpx-green.svg)](https://www.python-httpx.org/)
[![Pydantic](https://img.shields.io/badge/Schema-Pydantic_v2-red.svg)](https://docs.pydantic.dev/)

An enterprise-ready, asynchronous web scraper and data ETL pipeline built in Python. Designed for reliable data extraction, anti-bot resilience, schema validation, and multi-format export (styled Excel, CSV, JSON).

---

## 🌟 Key Highlights

- **High Performance Async I/O**: Powered by `httpx.AsyncClient` with connection pooling and non-blocking page fetching.
- **Strict Schema Validation**: Built on **Pydantic v2** to ensure 100% data integrity, type safety, and clean field casting.
- **Fault-Tolerant & Polite**:
  - Automatic exponential backoff and retry mechanism for transient network dropouts.
  - User-Agent header rotation & configurable rate-limiting delays to respect target servers.
- **Professional Multi-Format Export**:
  - **Excel (`.xlsx`)**: Auto-formatted with professional header palettes, auto-adjusted column widths, and proper cell types.
  - **CSV**: UTF-8 BOM encoded for seamless opening in Microsoft Excel without character corruption.
  - **JSON**: Clean, nested structured format ready for database ingestion or API consumers.

---

## 🏗️ Architecture

```
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│ Target Web Page │ ───>  │  Async Fetcher  │ ───>  │  HTML Parser    │
│  (E-Commerce)   │       │ (httpx + Retry) │       │ (BeautifulSoup) │
└─────────────────┘       └─────────────────┘       └─────────────────┘
                                                             │
                                                             ▼
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│ Multi-Export    │ <───  │ Data Validation │ <───  │ Raw Extracted   │
│ (Excel/CSV/JSON)│       │  (Pydantic v2)  │       │   Dictionary    │
└─────────────────┘       └─────────────────┘       └─────────────────┘
```

---

## 🚀 Quickstart

### 1. Clone & Install Dependencies

```bash
git clone https://github.com/your-username/ecommerce-scraper-pipeline.git
cd ecommerce-scraper-pipeline

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

### 2. Run the Pipeline

```bash
# Run with default settings (scrapes 2 pages and exports all formats)
python main.py

# Custom options: scrape 5 pages, polite 1.0s delay, export styled Excel only
python main.py --pages 5 --delay 1.0 --format excel --output-dir ./reports
```

### CLI Arguments

| Flag | Default | Description |
| :--- | :--- | :--- |
| `--pages` | `2` | Number of pagination pages to crawl |
| `--format` | `all` | Output format (`csv`, `json`, `excel`, `all`) |
| `--output-dir`| `output` | Target folder for exported files |
| `--delay` | `0.5` | Delay in seconds between requests |

---

## 📊 Sample Output Preview

```json
[
  {
    "title": "A Light in the Attic",
    "price": 51.77,
    "currency": "GBP",
    "rating": 3,
    "availability": "In stock",
    "product_url": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
    "image_url": "https://books.toscrape.com/media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg",
    "scraped_at": "2026-10-09T08:45:00.000Z"
  }
]
```

---

## 🛠️ Customization & Services

Need a scraper tailored for a specific platform (Amazon, Shopify, Real Estate, LinkedIn, etc.) with proxy integration, CAPTCHA solving, or headless browser automation (Playwright)?

Feel free to reach out for custom automation and scraping solutions!
