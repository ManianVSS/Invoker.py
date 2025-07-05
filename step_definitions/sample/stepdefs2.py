from core.decorators.stepdef import step_def
from core.utils.logger import logger, gui_info


@step_def("my sample step definition3")
def my_sample_step_definition3(context, step_data, gui=None, **kwargs):
    gui_info('Context is: {}'.format(str(context)), gui)
    gui_info('StepData is: {}'.format(str(step_data)), gui)
    context['var3'] = 3


@step_def("my sample step definition4")
def my_sample_step_definition4(context, step_data, gui=None, **kwargs):
    gui_info('Context is: {}'.format(str(context)), gui)
    gui_info('StepData is: {}'.format(str(step_data)), gui)
    context['var4'] = 4
