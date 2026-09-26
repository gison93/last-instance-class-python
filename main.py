import importlib
import sys

from dodo import Dodo

huey = Dodo("Huey")
dewey = Dodo("Dewey")

del huey
del dewey

importlib.reload(sys.modules['dodo'])

from dodo import Dodo

louie = Dodo("Louie")