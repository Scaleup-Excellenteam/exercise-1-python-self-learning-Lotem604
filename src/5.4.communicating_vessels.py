def generator_interleave(*iterable):
    """using for with longest size of iterables and making for on them
        each every time check the current iterable isn't index out of bound"""

    max_length = max([len(i) for i in iterable], default=0)

    for i in range(max_length):
        for it in iterable:
            if i < len(it):
                yield it[i]

# Add this line to fix the test:
interleave = generator_interleave


def main() -> None:
    print(list(generator_interleave('abc', [1, 2, 3], ('!', '@', '#'))))


if __name__ == '__main__':
    main()
