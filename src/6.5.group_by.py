"""Groups elements of an iterable based on the result of a function applied to each element."""
def group_by(f, iter1) -> dict:
    return_value = {}

    for it in iter1:
        key = f(it)
        tmp = return_value.get(key, [])
        tmp.append(it)

        return_value[key] = tmp
    return return_value


def main() -> None:
    print(group_by(len, ["hi", "bye", "yo", "try"]))


if __name__ == '__main__':
    main()
