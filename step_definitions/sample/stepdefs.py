from core.decorators.stepdef import step_def
from core.utils.logger import logger


@step_def("my sample step definition1")
def my_sample_step_definition1(context, step_data, **kwargs):
    logger.info('Context is: {}'.format(str(context)))
    logger.info('StepData is: {}'.format(str(step_data)))
    context['var1'] = 1


@step_def("my sample step definition2")
def my_sample_step_definition2(context, step_data, **kwargs):
    logger.info('Context is: {}'.format(str(context)))
    logger.info('StepData is: {}'.format(str(step_data)))
    context['var2'] = 2
