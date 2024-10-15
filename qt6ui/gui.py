import os

from PyQt6 import uic
from PyQt6.QtWidgets import *


# noinspection PyUnresolvedReferences
class InvokerGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        module_path = os.path.dirname(__file__)
        uic.loadUi(module_path + "/Invoker.ui", self)
        self.show()

        self.action_about.triggered.connect(self.handle_about)

    def handle_about(self):
        message_box = QMessageBox(self)
        message_box.setWindowTitle("About")
        message_box.setText(
            "Invoker.py is a python port of Invoker tool which lets you invoke actions on different contexts.")
        message_box.exec()


def main():
    app = QApplication([])
    window = InvokerGUI()
    app.exec()
    return window


if __name__ == '__main__':
    main()
