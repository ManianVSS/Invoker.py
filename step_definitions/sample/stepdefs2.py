from core.decorators.stepdef import step_def


@step_def("my sample step definition3")
def my_sample_step_definition3(context=None, **kwargs):
    print('Context is:', str(context))
    context['var3'] = 3


@step_def("my sample step definition4")
def my_sample_step_definition4(context=None, **kwargs):
    print('Context is:', str(context))
    context['var4'] = 4
