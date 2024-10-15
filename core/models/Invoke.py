from .Step import Step


class Invoke:
    def __init__(self, name=None, steps=None):
        self.name = name
        self.steps = [Step(**step) for step in steps]
