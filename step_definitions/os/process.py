import os
import subprocess
import json

from core.decorators.stepdef import step_def
from core.utils.variableutil import replace_variables_in_str_array, replace_variables


@step_def("run process")
def run_process(context=None, **kwargs):
    replaced_command = replace_variables_in_str_array(context.step.data.command, context, context.step.data,
                                                      os.environ.copy())
    completed_process = subprocess.run(replaced_command, capture_output=True)
    return completed_process


@step_def("spawn process")
def spawn_process(context=None, **kwargs):
    replaced_command = replace_variables(context.step.data.command, context, context.step.data, os.environ.copy())
    replaced_arguments = [replaced_command]

    if context.step.data.arguments:
        for arg in context.step.data.arguments:
            replaced_arguments.append(replace_variables(arg, context, context.step.data, os.environ.copy()))
    process_id = os.spawnv(os.P_NOWAIT, replaced_command, replaced_arguments)
    return process_id
