from urllib.parse import urlparse, parse_qs
from playwright.sync_api import Page
import json

def fetch_uniqlo_product(page: Page, url: str):
    """
    Scraper para extraer datos de un producto de UNIQLO, con manejo de errores para selectores faltantes.

    Args:
        page (Page): Instancia de Playwright para interactuar con la página.
        url (str): URL del producto.

    Returns:
        dict: Información del producto (nombre, precio, oferta, colores, tallas, url).
    """
    try:
        # Navegar a la URL
        page.goto(url)
        
        # Esperar que el DOM cargue
        page.wait_for_selector("body", timeout=10000)

        # Nombre del producto
        try:
            product_name_selector = "h1.fr-ec-display--display5"
            product_name_element = page.query_selector(product_name_selector)
            product_name = product_name_element.inner_text() if product_name_element else "Producto no encontrado"
        except Exception as e:
            product_name = None
            print(f"Error al extraer el nombre del producto: {e}")

        # Precio del producto
        try:
            price_selector = "p.fr-ec-price-text--large"
            price_element = page.query_selector(price_selector)
            price_text = price_element.inner_text() if price_element else "0"
            price = float(price_text.replace("€", "").replace(",", ".").strip())
        except Exception as e:
            price = None
            print(f"Error al extraer el precio del producto: {e}")

        # Colores y tallas disponibles
        variants = []
        try:
            # Selector específico para los colores
            color_selector = "#product-color-picker input.fr-ec-chip__input"
            color_code_in_url = None
            if "colorDisplayCode=" in url:
                color_code_in_url = url.split("colorDisplayCode=")[1].split("&")[0]

            for color_element in page.query_selector_all(color_selector):
                color_name = color_element.get_attribute("aria-label")
                color_code = color_element.get_attribute("value")
                image_selector = "img.fr-ec-chip__default-image"
                image_element = color_element.query_selector(image_selector)
                image_url = image_element.get_attribute("src") if image_element else None

                # Si la URL contiene un código de color, solo extraer esa variante
                if color_code_in_url and color_code != color_code_in_url:
                    continue

                sizes = []
                # Esperar un tiempo adicional para asegurarse de que la página se haya cargado completamente
                page.wait_for_timeout(2000)  # Esperar 5 segundos

                # Selector específico para las tallas
                size_selector = "#product-size-picker input.fr-ec-chip__input"
                for size_element in page.query_selector_all(size_selector):
                    size_name = size_element.get_attribute("aria-label")
                    size_status = "unavailable" in size_name.lower() if size_name else False
                    sizes.append({
                        "size": size_name.replace(" (unavailable)", "") if size_name else "Talla desconocida",
                        "available": not size_status
                    })

                variants.append({
                    "color_name": color_name,
                    "color_code": color_code,
                    "sizes": sizes,
                    "image_url": image_url
                })

                # Si la URL contiene un código de color, salir del bucle después de encontrar la variante
                if color_code_in_url:
                    break
        except Exception as e:
            print(f"Error al extraer los colores y tallas: {e}")

        product_info = {
            "store": "UNIQLO",
            "product_name": product_name,
            "price": price,
            "variants": variants,
            "url": url,
        }
    
        # Guardar la información del producto en un archivo JSON
        with open("uniqlo.json", "w", encoding="utf-8") as f:
            json.dump(product_info, f, ensure_ascii=False, indent=4)
        return product_info
    except Exception as e:
        print(f"Error al extraer datos de UNIQLO: {e}")
        return None
