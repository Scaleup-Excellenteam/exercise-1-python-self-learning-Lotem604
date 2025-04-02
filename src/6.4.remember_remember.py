import matplotlib.image as ping

""" Reads an image from the specified path and extracts non-white pixel values, converting them to a string."""
def remember_remember(path: str) -> str:
    image = ping.imread(path)
    height, width = image.shape

    return "".join(chr(y) for x in range(width) for y in range(height) if image[y, x] != 1)


def main() -> None:
    path = '../exelentim/exercise-1-python-self-learning-Lotem604/content/week06/resources/code.png'
    print(remember_remember(path))


if __name__ == '__main__':
    main()
