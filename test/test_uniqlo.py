import unittest
from unittest.mock import MagicMock
from stores.uniqlo import fetch_uniqlo_product  # Asegúrate de que 'fetch_uniqlo_product' es el nombre correcto de la función

class TestUniqloScraper(unittest.TestCase):
    def test_scrape_product(self):
        # Configurar los mocks
        mock_page = MagicMock()
        mock_page.goto = MagicMock()
        mock_page.wait_for_selector = MagicMock()
        mock_page.query_selector = MagicMock()
        
        # Mock de los selectores
        mock_product_name_element = MagicMock()
        mock_product_name_element.inner_text.return_value = "h1.fr-ec-display--display5"
        mock_price_element = MagicMock()
        mock_price_element.inner_text.return_value = "19,99€"
        
        mock_page.query_selector.side_effect = lambda selector: {
            '.product-name-selector': mock_product_name_element,
            '.price-selector': mock_price_element
        }[selector]        
        # Llamar al método que se desea probar
        url = "https://www.uniqlo.com/es/es/products/E470077-000/00?colorDisplayCode=57&sizeDisplayCode=004"
        result = fetch_uniqlo_product(mock_page, url)
        

        
        # Verificar el resultado
        expected_result = {
            "store": "UNIQLO",
            "product_name": "Producto de prueba",
            "price": 19.99,
            "url": url,
        }
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()