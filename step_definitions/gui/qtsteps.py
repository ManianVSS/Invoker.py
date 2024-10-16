import os

from PyQt6.QtWidgets import QMessageBox

from core.decorators.stepdef import step_def
from core.utils.variableutil import replace_variables


@step_def("display message")
def display_message(context=None, gui=None, **kwargs):
    replaced_title = replace_variables(context.step.data.title if context.step.data.title else "Message!!", context,
                                       context.step.data, os.environ.copy())
    replaced_message = replace_variables(context.step.data.message, context, context.step.data, os.environ.copy())
    gui.showMessageBox.emit(replaced_title, replaced_message)
