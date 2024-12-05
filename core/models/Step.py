from core.models.Context import VarClass


class Step:
    def __init__(self, name=None, data=None, output_ref=None):
        self.name = name
        variable_dict = VarClass()
        variable_dict.update(data if data else {})
        self.data = variable_dict
        self.output_ref = output_ref
