def piece_of_cake(prices, optionals=None, **products):
    """Calculate the total price for a recipe, excluding optional products."""
    if optionals is None:
        optionals = []
    
    total_price = 0

    for product_name, weight in products.items():
        if product_name in optionals:
            continue
        if product_name not in prices:
            raise ValueError(f"Missing price for product: {product_name}")
        total_price += prices[product_name] * (weight / 100)

    return total_price


def main() -> None:
    prices = {'chocolate': 18, 'milk': 8}
    print(piece_of_cake(prices, chocolate=200, milk=100))
    print(piece_of_cake(prices, optionals=['milk'], chocolate=300))
    print(piece_of_cake({}))


if __name__ == '__main__':
    main()
