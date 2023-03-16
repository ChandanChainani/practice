import os
import json
from importlib import import_module, reload
# reloader
def reloader():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(current_directory, "loader.json")
    with open(filename) as f:
        config = json.load(f)
        for module in config.get("modules"):
            try:
                reload(import_module(module))
            except Exception as e:
                print(e)

