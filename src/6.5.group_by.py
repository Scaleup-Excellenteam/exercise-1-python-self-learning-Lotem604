import inspect

"""Groups elements of an iterable based on the result of a function applied to each element."""
def group_by(f, iter1) -> dict:
    if not callable(f):
        raise TypeError(f"The provided function {f} is not callable.")

    return_value = {}

    for it in iter1:
        try:
            key = f(it)
        except Exception as e:
            raise TypeError(f"Function {f.__name__} cannot be applied to element {it}: {e}")

        tmp = return_value.get(key, [])
        tmp.append(it)
        return_value[key] = tmp

    return return_value

def main() -> None:
    print(group_by(len, ["hi", "bye", "yo", "try"]))

if __name__ == '__main__':
    main()
