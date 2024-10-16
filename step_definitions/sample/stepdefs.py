from core.decorators.stepdef import step_def


@step_def("my sample step definition1")
def my_sample_step_definition1(context=None, **kwargs):
    print('Context is:', str(context))
    context['var1'] = 1


@step_def("my sample step definition2")
def my_sample_step_definition2(context=None, **kwargs):
    print('Context is:', str(context))
    context['var2'] = 2
