import os
from functools import partial
from pathlib import Path
from threading import Thread

from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import *

from core.models.Context import Context
from core.runner.main import init_step_definitions, run_invoke, read_environments
from core.utils.logger import logger


def clear_layout(layout):
    logger.debug("-- -- input layout: " + str(layout))
    for i in reversed(range(layout.count())):
        layout_item = layout.itemAt(i)
        if layout_item.widget() is not None:
            widget_to_remove = layout_item.widget()
            logger.debug("found widget: " + str(widget_to_remove))
            widget_to_remove.setParent(None)
            layout.removeWidget(widget_to_remove)
        elif layout_item.spacerItem() is not None:
            logger.debug("found spacer: " + str(layout_item.spacerItem()))
        else:
            layout_to_remove = layout.itemAt(i)
            logger.debug("-- found Layout: " + str(layout_to_remove))
            clear_layout(layout_to_remove)


# noinspection PyUnresolvedReferences
class InvokerGUI(QMainWindow):
    showMessageBox = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.invokes = None
        self.environments = None

        module_path = os.path.dirname(__file__)
        uic.loadUi(module_path + "/Invoker.ui", self)
        self.tab_invoke.layout = QGridLayout(self.tab_invoke)
        self.combobox_contexts.currentIndexChanged.connect(self.environment_switched)

        init_step_definitions('step_definitions')
        self.default_context = Context()
        self.context = self.default_context
        self.load_environments()

        self.load_invokes()

        self.show()

        self.action_about.triggered.connect(self.handle_about)

        # combobox_contexts

    def load_invokes(self):
        src = "invokes"
        self.invokes = []
        clear_layout(self.tab_invoke.layout)
        self.showMessageBox.connect(self.on_show_message_box)

        for invoke_file in Path(src).glob("**/*.yaml"):
            invoke_name = invoke_file.stem
            self.invokes.append(invoke_file)
            invoke_button = QPushButton(invoke_name, self)
            invoke_button.clicked.connect(partial(self.trigger_invoke, invoke_name=invoke_file))
            self.tab_invoke.layout.addWidget(invoke_button)

    def load_environments(self):
        self.environments = read_environments('environments')
        self.combobox_contexts.clear()
        self.combobox_contexts.addItems(self.environments.keys())

    def environment_switched(self):
        environment_name = self.combobox_contexts.currentText()
        if environment_name in self.environments.keys():
            self.context = self.environments[environment_name]
        else:
            self.context = self.default_context

    def trigger_invoke(self, invoke_name):
        thread = Thread(target=run_invoke, args=(invoke_name, self.context, self))
        thread.start()
        return thread

    def handle_about(self):
        message_box = QMessageBox(self)
        message_box.setWindowTitle("About")
        message_box.setText(
            "Invoker.py is a python port of Invoker tool which lets you invoke actions on different contexts.")
        message_box.exec()

    # @pyqtSlot(str, str)
    def on_show_message_box(self, title, text):
        # noinspection PyTypeChecker
        QMessageBox.information(self, title, text)


def main():
    app = QApplication([])
    window = InvokerGUI()
    app.exec()
    return window


if __name__ == '__main__':
    main()
