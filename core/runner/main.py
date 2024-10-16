import importlib
import importlib.util
import os
from copy import deepcopy
from threading import Thread

import yaml

from ..models.Context import Context
from ..models.Invoke import Invoke
from . import step_definition_mapping


def load_invoke_file(invoke_file):
    with open(invoke_file, "r") as stream:
        try:
            invoke_raw_object = yaml.safe_load(stream)
            feature_object = Invoke(**invoke_raw_object)
            return feature_object
        except yaml.YAMLError as exc:
            print(exc)


def get_python_files(src='step_definitions'):
    cwd = os.getcwd()
    py_files = []
    for root, dirs, files in os.walk(src):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(cwd, root, file))
    return py_files


def dynamic_import(module_name_to_import, py_path):
    module_spec = importlib.util.spec_from_file_location(module_name_to_import, py_path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module


def dynamic_import_from_src(src, star_import=False):
    my_py_files = get_python_files(src)
    for py_file in my_py_files:
        module_name = os.path.split(py_file)[-1].strip(".py")
        imported_module = dynamic_import(module_name, py_file)
        if star_import:
            for obj in dir(imported_module):
                globals()[obj] = imported_module.__dict__[obj]
        else:
            globals()[module_name] = imported_module
    return


def init_step_definitions(step_def_package='step_definitions'):
    # Search for python modules in step definitions folder
    step_definition_module_python_files = get_python_files(step_def_package)

    # Scan for each python module if it has step definitions, add them to step definition mapping
    for py_file in step_definition_module_python_files:
        module_name = os.path.split(py_file)[-1].strip(".py")
        imported_step_def_module = dynamic_import(module_name, py_file)


def run_invoke(invoke_name, context=None, gui=None):
    if context is None:
        context = Context()

    # Load the invoke file to run
    invoke = load_invoke_file(invoke_name)

    print('Running invoke ', str(invoke.name))

    try:
        for step in invoke.steps:
            print('Running step ', str(step.name))
            step_to_call = step.name.strip()
            if step_to_call in step_definition_mapping.keys():
                # step_context = deepcopy(context)
                context.invoke_name = invoke.name
                context["step"] = step
                output = step_definition_mapping[step_to_call](context=context, gui=gui)
                if step.output_ref:
                    context[step.output_ref] = output
            else:
                print("Step definition mapping for %s could not be found", step_to_call)
    except Exception as e:
        print("Exception occurred when running Invoke: ", e)


def trigger_invoke(invoke_name, context=None, gui=None):
    if context is None:
        context = Context()

    thread = Thread(target=run_invoke, args=(invoke_name, context, gui))
    thread.start()
    return thread
