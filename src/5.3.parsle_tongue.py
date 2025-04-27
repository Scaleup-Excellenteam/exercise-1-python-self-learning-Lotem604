import re

def parsle_tongue(path="logo.jpg"):
    """
    Reads a binary file in chunks and extracts secret messages.

    Args:
        path (str): Path to the binary file (default is 'logo.jpg').

    Yields:
        str: Each extracted message, decoded from bytes to string, without the ending '!'.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        UnicodeDecodeError: If decoding from bytes to string fails.
    """
    with open(path, "rb") as logo:
        tokens = logo.read(1024)
        while tokens:
            encrypted = re.findall(b'[a-z]{5,}!', tokens)

            for token in encrypted:
                yield token[:-1].decode()

            tokens = logo.read(1024)

def main() -> None:
    root = '../exelentim/exercise-1-python-self-learning-Lotem604/content/week05/resources/logo.jpg'
    for element in parsle_tongue(root):
        print(element)

if __name__ == '__main__':
    main()
