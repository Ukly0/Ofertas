def is_offer(current_price, original_price, discount_threshold=20):
    """
    Verifica si un producto cumple con el descuento mínimo requerido.

    Args:
        current_price (float): Precio actual.
        original_price (float): Precio original.
        discount_threshold (float): Descuento mínimo en porcentaje.

    Returns:
        bool: True si es una oferta, False en caso contrario.
    """
    try:
        discount = ((original_price - current_price) / original_price) * 100
        return discount >= discount_threshold
    except ZeroDivisionError:
        print("El precio original no puede ser 0.")
        return False
