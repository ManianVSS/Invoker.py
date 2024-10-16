import os

from core.decorators.stepdef import step_def
from core.utils.variableutil import replace_variables


@step_def("echo")
def echo_message(context=None, **kwargs):
    replaced_message = replace_variables(context.step.data['message'], context, context.step.data, os.environ.copy())
    print(replaced_message)
