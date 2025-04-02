import time

"""Measure the execution time of a function using a high-resolution timer."""
def running_2000(f, *args, **kwargs):
    start = time.time()
    f(*args, **kwargs)
    return time.time() - start


def main() -> None:
    print(f'time = {running_2000(zip, [1, 2, 3], [4, 5, 6])}')


if __name__ == '__main__':
    main()
