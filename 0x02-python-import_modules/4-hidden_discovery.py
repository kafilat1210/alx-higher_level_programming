#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names_mod = dir(hidden_4)
    filtered_names = [name for name in names_mod if not name.startswith("__")]

    for name in filtered_names:
        print(name)
