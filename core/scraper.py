import os
import sys
from playwright.sync_api import sync_playwright
from stores.uniqlo import fetch_uniqlo_product
from stores.zara import fetch_zara_product

def scrape_product(url):
    """
    Scraper genérico que delega a funciones específicas según la tienda.

    Args:
        url (str): URL del producto.

    Returns:
        dict: Información del producto o None si falla.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Delegar según la tienda
        if "uniqlo.com" in url:
            result = fetch_uniqlo_product(page, url)
        elif "zara.com" in url:
            result = fetch_zara_product(page, url)
        else:
            print(f"Tienda no soportada para la URL: {url}")
            result = None

        browser.close()
        return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python scraper.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    product_info = scrape_product(url)
    print(product_info)