#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    normalnames = []

    for name in names:
        if name.startswith("__") is not True:
            normalnames.append(name)
    normalnames = sorted(normalnames)
    for name in normalnames:
        print(name)
