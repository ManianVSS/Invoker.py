import os
from functools import partial
from pathlib import Path

from PyQt6 import uic, QtCore
from PyQt6.QtCore import pyqtSlot, pyqtSignal
from PyQt6.QtWidgets import *

from core.models.Context import Context
from core.runner.main import init_step_definitions, run_invoke, trigger_invoke


# noinspection PyUnresolvedReferences
class InvokerGUI(QMainWindow):
    showMessageBox = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        module_path = os.path.dirname(__file__)
        uic.loadUi(module_path + "/Invoker.ui", self)

        init_step_definitions('step_definitions')
        context = Context()

        src = "invokes"
        cwd = os.getcwd()
        invokes = []
        self.tab_invoke.layout = QGridLayout(self.tab_invoke)

        self.showMessageBox.connect(self.on_show_message_box)

        for root, dirs, files in os.walk(src):
            for file in files:
                if file.endswith(".yaml"):
                    invoke_file = os.path.join(cwd, root, file)
                    invoke_name = Path(file).stem
                    invokes.append(invoke_file)
                    invoke_button = QPushButton(invoke_name, self)
                    invoke_button.clicked.connect(
                        partial(trigger_invoke, invoke_name=invoke_file, context=context, gui=self))
                    self.tab_invoke.layout.addWidget(invoke_button)

        self.show()

        self.action_about.triggered.connect(self.handle_about)

    def handle_about(self):
        message_box = QMessageBox(self)
        message_box.setWindowTitle("About")
        message_box.setText(
            "Invoker.py is a python port of Invoker tool which lets you invoke actions on different contexts.")
        message_box.exec()

    # @pyqtSlot(str, str)
    def on_show_message_box(self, title, text):
        QMessageBox.information(self, title, text)


def main():
    app = QApplication([])
    window = InvokerGUI()
    app.exec()
    return window


if __name__ == '__main__':
    main()
