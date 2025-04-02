"""Process a given string to create a dictionary with words as keys and their lengths as values."""
def long_cat_is_long(orel: str) -> dict[str: int]:
    stringReturn = ''.join([i if i.isalpha() or i.isspace() else "" for i in orel]).split()
    wordsReturn = {word: len(word) for word in stringReturn}
    return wordsReturn


def main() -> None:
    text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """
    print(long_cat_is_long(text))


if __name__ == '__main__':
    main()
