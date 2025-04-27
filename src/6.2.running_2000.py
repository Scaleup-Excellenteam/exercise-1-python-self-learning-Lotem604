import time
import inspect

def running_2000(f, *args, **kwargs):
    """
    Measure the execution time of a given function using a high-resolution timer.

    Args:
        f (Callable): The function to measure.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.

    Returns:
        float: The execution time in seconds.

    Raises:
        TypeError: If the provided function cannot be called with the given arguments.
    """
    if not callable(f):
        raise TypeError(f"The provided object {f} is not callable.")

    try:
        signature = inspect.signature(f)
        signature.bind(*args, **kwargs)
    except TypeError as e:
        raise TypeError(f"Function cannot be called with the provided arguments: {e}")

    start = time.perf_counter() 
    f(*args, **kwargs)
    end = time.perf_counter()

    return end - start

def main() -> None:
    print(f'time = {running_2000(zip, [1, 2, 3], [4, 5, 6])}')

if __name__ == '__main__':
    main()
