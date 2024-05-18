def decimal_to_int(price: float, decimal: int) -> int:
    """Converts a price and decimal to an integer.

    Args:
        price: The price, in dollars.
        decimal: The decimal part of the price, in cents.

    Returns:
        The price, in cents, as an integer.
    """
    if not isinstance(price, (int, float)) or not isinstance(decimal, int):
        raise ValueError("Invalid input types. 'price' must be a number and 'decimal' must be an integer.")

    if decimal < 0 or decimal >= 100:
        raise ValueError("Invalid decimal value. It must be between 0 and 99.")

    return int(price) * 100 + decimal

# Example usage:
total_cents = decimal_to_int(19.99, 99)
print(total_cents)  # Output: 1999
