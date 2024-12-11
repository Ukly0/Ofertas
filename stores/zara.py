from playwright.sync_api import Page

def fetch_zara_product(page: Page, url: str):
    """
    Scraper para extraer datos de un producto de Zara.

    Args:
        page (Page): Instancia de Playwright para interactuar con la página.
        url (str): URL del producto.

    Returns:
        dict: Información del producto (nombre, precio, url), o None si falla.
    """
    try:
        page.goto(url)

        # Selectores específicos de Zara
        product_name_selector = "h1.product-detail-name"
        price_selector = "span.current-price"

        # Esperar que los elementos existan
        page.wait_for_selector(product_name_selector, timeout=5000)
        page.wait_for_selector(price_selector, timeout=5000)

        # Extraer información
        product_name = page.query_selector(product_name_selector).inner_text()
        price_text = page.query_selector(price_selector).inner_text()

        # Convertir precio a número
        price = float(price_text.replace("€", "").replace(",", ".").strip())

        return {
            "store": "ZARA",
            "product_name": product_name,
            "price": price,
            "url": url,
        }
    except Exception as e:
        print(f"Error al extraer datos de Zara: {e}")
        return None
