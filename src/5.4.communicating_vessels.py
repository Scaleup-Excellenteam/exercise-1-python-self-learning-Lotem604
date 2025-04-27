def interleave(*iterable):
    """
    Interleave elements from multiple iterables.

    Args:
        *iterable: Any number of iterable objects.

    Yields:
        Elements from the iterables, taken one by one in order, until all are exhausted.
    """
    max_length = max((len(i) for i in iterable), default=0)

    for i in range(max_length):
        for it in iterable:
            if i < len(it):
                yield it[i]

def main() -> None:
    print(list(interleave('abc', [1, 2, 3], ('!', '@', '#'))))

if __name__ == '__main__':
    main()
