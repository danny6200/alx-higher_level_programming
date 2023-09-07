#!/usr/bin/python3
import importlib
import sys

module = importlib.import_module("hidden_4")

module_names = dir(module)

filtered_names = sorted(name for name in module_names if not name.startswith('__'))

for name in filtered_names:
    print(name)
