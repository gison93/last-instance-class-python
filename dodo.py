import inspect
import os

class Dodo:
    instance_count = 0
    instanced_once = False

    def __init__(self, name):
        Dodo.instanced_once = True
        Dodo.instance_count += 1
        self.name = name

    def __del__(self):
            Dodo.instance_count -= 1
            if Dodo.instance_count == 0 and Dodo.instanced_once:
                Dodo.delete()

    @classmethod
    def delete(cls):
        if cls.__name__ in globals():
            print(f"Deleting class {cls.__name__}")
            del globals()[cls.__name__]
            filepath = inspect.getfile(cls)
            os.remove(filepath)