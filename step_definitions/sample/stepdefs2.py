from core.decorators.stepdef import step_def
from core.utils.logger import logger


@step_def("my sample step definition3")
def my_sample_step_definition3(context, step_data, **kwargs):
    logger.info('Context is: {}'.format(str(context)))
    logger.info('StepData is: {}'.format(str(step_data)))
    context['var3'] = 3


@step_def("my sample step definition4")
def my_sample_step_definition4(context, step_data, **kwargs):
    logger.info('Context is: {}'.format(str(context)))
    logger.info('StepData is: {}'.format(str(step_data)))
    context['var4'] = 4
