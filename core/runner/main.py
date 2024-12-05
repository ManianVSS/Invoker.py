import configparser
import json
from pathlib import Path
from threading import Thread

import yaml

from . import step_definition_mapping
from ..models.Context import Context
from ..models.Invoke import Invoke
from ..utils.datautils import parse_value, deep_update
from ..utils.importutils import get_python_files, import_module_from_file
from ..utils.logger import logger


def load_invoke_file(invoke_file):
    with open(invoke_file, "r") as stream:
        try:
            invoke_raw_object = yaml.safe_load(stream)
            feature_object = Invoke(**invoke_raw_object)
            return feature_object
        except yaml.YAMLError as exc:
            logger.info(exc)


def init_step_definitions(step_def_package='step_definitions'):
    # Search for python modules in step definitions folder
    step_definition_module_python_files = get_python_files(step_def_package)

    # Scan for each python module if it has step definitions, add them to step definition mapping
    for py_file in step_definition_module_python_files:
        module_name = Path(py_file).stem
        import_module_from_file(module_name, py_file)


def run_invoke(invoke_name, context=None, gui=None):
    if context is None:
        context = Context()

    # Load the invoke file to run
    invoke = load_invoke_file(invoke_name)

    logger.info('Running invoke {}'.format(str(invoke.name)))

    try:
        for step in invoke.steps:
            logger.info('Running step {}'.format(str(step.name)))
            step_to_call = step.name.strip()
            if step_to_call in step_definition_mapping.keys():
                output = step_definition_mapping[step_to_call](context=context, step_data=step.data, gui=gui)
                if step.output_ref:
                    context[step.output_ref] = output
            else:
                logger.info("Step definition mapping for {} could not be found".format(step_to_call))
    except Exception as e:
        logger.error("Exception occurred when running Invoke: {}".format(e))


def trigger_invoke(invoke_name, context=None, gui=None):
    if context is None:
        context = Context()

    thread = Thread(target=run_invoke, args=(invoke_name, context, gui))
    thread.start()
    return thread


def read_environments(properties_folder: str) -> dict[str, object]:
    environments: dict[str, Context] = {}
    folder_path = Path(properties_folder) if properties_folder else Path('environments')
    # Path(os.path.expanduser('~'), ".invoker")

    for environment_file in folder_path.glob("**/*.ini"):
        config = configparser.RawConfigParser()
        config.optionxform = str
        config.read(environment_file)
        source_dict = {}
        for section in config.sections():
            source_dict[section] = {k: parse_value(v) for k, v in config[section].items()}
        deep_update(environments, source_dict)

    for environment_file in folder_path.glob("**/*.json"):
        with open(environment_file, "r") as stream:
            parsed_properties = json.load(stream)
            deep_update(environments, parsed_properties)

    for environment_file in folder_path.glob("**/*.yaml"):
        with open(environment_file, "r") as stream:
            parsed_properties = yaml.safe_load(stream.read())
            deep_update(environments, parsed_properties)

    for environment in environments.keys():
        environments[environment] = Context(**environments[environment])
    return environments
