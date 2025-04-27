def piece_of_cake(prices, optionals=None, **products):
    """Calculate the total price for a recipe, excluding optional products."""
    if optionals is None:
        optionals = []
    
    try:
        total_price = sum(
            prices[product_name] * (weight / 100)
            for product_name, weight in products.items()
            if product_name not in optionals
        )
    except KeyError as e:
        raise ValueError(f"Missing price for product: {e.args[0]}")

    return total_price

def main() -> None:
    prices = {'chocolate': 18, 'milk': 8}
    print(piece_of_cake(prices, chocolate=200, milk=100))
    print(piece_of_cake(prices, optionals=['milk'], chocolate=300))
    print(piece_of_cake({}))

if __name__ == '__main__':
    main()
