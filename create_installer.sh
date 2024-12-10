#!/bin/bash
source .venv/bin/activate

rm -rf build/ dist/
pyinstaller --hidden-import core.decorators.stepdef --hidden-import core.models.Context --hidden-import core.models.Invoke --hidden-import core.models.Step --hidden-import core.runner.main --hidden-import core.utils.datautils --hidden-import core.utils.importutils --hidden-import core.utils.logger  --hidden-import core.utils.process  --hidden-import core.utils.variableutil --add-data "qt6ui/Invoker.ui:qt6ui/"  --contents-directory lib -n invoker run.py

cp -r core dist/invoker
cp -r environments dist/invoker
cp -r invokes dist/invoker
cp -r step_definitions dist/invoker

cd dist/ || exit
tar -czvf invoker.tar.gz invoker
cd - || exit

