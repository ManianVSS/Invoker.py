import os

from core.decorators.stepdef import step_def
from core.utils.logger import logger, gui_info
from core.utils.variableutil import replace_variables


@step_def("echo")
def echo_message(context, step_data, gui=None, **kwargs):
    replaced_message = replace_variables(step_data['message'], context, step_data, os.environ.copy())
    gui_info(replaced_message, gui)
