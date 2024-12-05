import os

from core.decorators.stepdef import step_def
from core.utils.variableutil import replace_variables


@step_def("display message")
def display_message(context, step_data, gui=None, **kwargs):
    replaced_title = replace_variables(step_data.title if step_data.title else "Message!!", context,
                                       step_data, os.environ.copy())
    replaced_message = replace_variables(step_data.message, context, step_data, os.environ.copy())
    gui.showMessageBox.emit(replaced_title, replaced_message)
