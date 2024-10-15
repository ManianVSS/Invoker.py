from core.runner.main import *

init_step_definitions('step_definitions')

run_invoke('invokes/TestInvoke1.yaml')
run_invoke('invokes/TestInvoke2.yaml')
