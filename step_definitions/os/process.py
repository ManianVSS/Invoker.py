import os
import subprocess

from core.decorators.stepdef import step_def
from core.utils.logger import logger
from core.utils.variableutil import replace_variables_in_str_array, replace_variables


@step_def("run process")
def run_process(context, step_data, **kwargs):
    replaced_command = replace_variables_in_str_array(step_data.command, context, step_data,
                                                      os.environ.copy())
    logger.debug("Going to run process {}".format(replaced_command))
    completed_process = subprocess.run(replaced_command, capture_output=True)
    return completed_process


@step_def("spawn process")
def spawn_process(context, step_data, **kwargs):
    replaced_command = replace_variables(step_data.command, context, step_data, os.environ.copy())
    logger.debug("Going to spawn process {}".format(replaced_command))
    process_id = subprocess.Popen(replaced_command)
    return process_id.pid
