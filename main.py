import sys

from PyQt5 import QtWidgets

from ui_main import Application_form

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Application_form()
    sys.exit(app.exec())