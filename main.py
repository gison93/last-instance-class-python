import glob
import importlib.util
import sys

from dodo import Dodo

huey = Dodo("Huey")
dewey = Dodo("Dewey")

del huey
del dewey

pyc_path = glob.glob("__pycache__/dodo*.pyc")[0]
spec = importlib.util.spec_from_file_location("dodo", pyc_path)
dodo_module = importlib.util.module_from_spec(spec)
sys.modules["dodo"] = dodo_module
spec.loader.exec_module(dodo_module)

from dodo import Dodo

louie = Dodo("Louie")
print("Louie lives!")