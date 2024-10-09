from PyQt6.QtWidgets import *

from gui import InvokerGUI


def main():
    app = QApplication([])
    window = InvokerGUI()
    app.exec()


if __name__ == '__main__':
    main()
