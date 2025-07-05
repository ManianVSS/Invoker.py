from core.decorators.stepdef import step_def
from core.utils.logger import logger, gui_info


@step_def("my sample step definition1")
def my_sample_step_definition1(context, step_data, gui=None, **kwargs):
    gui_info('Context is: {}'.format(str(context)), gui)
    gui_info('StepData is: {}'.format(str(step_data)), gui)
    context['var1'] = 1


@step_def("my sample step definition2")
def my_sample_step_definition2(context, step_data, gui=None, **kwargs):
    gui_info('Context is: {}'.format(str(context)), gui)
    gui_info('StepData is: {}'.format(str(step_data)), gui)
    context['var2'] = 2
