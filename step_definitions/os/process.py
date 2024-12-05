import os
import subprocess

from core.decorators.stepdef import step_def
from core.utils.variableutil import replace_variables_in_str_array, replace_variables


@step_def("run process")
def run_process(context, step_data, **kwargs):
    replaced_command = replace_variables_in_str_array(step_data.command, context, step_data,
                                                      os.environ.copy())
    completed_process = subprocess.run(replaced_command, capture_output=True)
    return completed_process


@step_def("spawn process")
def spawn_process(context, step_data, **kwargs):
    replaced_command = replace_variables(step_data.command, context, step_data, os.environ.copy())
    replaced_arguments = [replaced_command]

    if step_data.arguments:
        for arg in step_data.arguments:
            replaced_arguments.append(replace_variables(arg, context, step_data, os.environ.copy()))
    process_id = os.spawnv(os.P_NOWAIT, replaced_command, replaced_arguments)
    return process_id
