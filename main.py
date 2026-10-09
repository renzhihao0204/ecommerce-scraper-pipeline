import sys
import argparse
import asyncio
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from scraper import ProductScraper
from export import export_to_csv, export_to_json, export_to_excel

async def main():
    parser = argparse.ArgumentParser(
        description="Production-grade Async E-commerce Scraping & Clean Export Pipeline."
    )
    parser.add_argument(
        "--pages",
        type=int,
        default=2,
        help="Number of pages to scrape (default: 2)",
    )
    parser.add_argument(
        "--format",
        choices=["csv", "json", "excel", "all"],
        default="all",
        help="Export format (default: all)",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="output",
        help="Directory to save scraped results (default: output)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Polite delay between page requests in seconds (default: 0.5)",
    )

    args = parser.parse_args()
    output_dir = Path(args.output_dir)

    print("=" * 60)
    print("🚀 Starting E-commerce Scraper Pipeline")
    print(f"Target Pages: {args.pages} | Formats: {args.format} | Delay: {args.delay}s")
    print("=" * 60)

    scraper = ProductScraper(delay=args.delay)
    try:
        products = await scraper.scrape(max_pages=args.pages)
    finally:
        await scraper.close()

    if not products:
        print("[Notice] No products scraped. Exiting.")
        return

    print(f"\n[Success] Scraped total {len(products)} products. Exporting...")

    if args.format in ["csv", "all"]:
        export_to_csv(products, output_dir / "products.csv")

    if args.format in ["json", "all"]:
        export_to_json(products, output_dir / "products.json")

    if args.format in ["excel", "all"]:
        export_to_excel(products, output_dir / "products.xlsx")

    print("\n🎉 Pipeline completed successfully!")

if __name__ == "__main__":
    asyncio.run(main())
