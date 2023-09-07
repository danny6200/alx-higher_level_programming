#!/usr/bin/python3
if __name__ == "__main__":
    import importlib
    import sys

    mod = importlib.import_module("hidden_4")

    mod_names = dir(mod)

    f_names = sorted(name for name in mod_names if not name.startswith('__'))

    for name in f_names:
        print(name)
