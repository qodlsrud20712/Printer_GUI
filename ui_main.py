import subprocess
import time

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QGridLayout, QAction, qApp, QMessageBox
from pywinauto.application import Application
from PyQt5 import uic

dir = ["C:/Zebra Technologies/ZebraDesigner 3/bin.net/ZebraDesigner.exe",
       "C:/Program Files (x86)/Zebra Technologies/Zebra Setup Utilities/App/PrnUtils.exe"]
ZD_dir = dir[0]
ZSU_dir = dir[1]


class Application_form():

    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("Test.ui")
        self.ui.ZSU_btn.clicked.connect(self.Go_to_ZSU)
        self.ui.ZD_btn.clicked.connect(self.Go_to_ZD)
        self.ui.Create_btn.clicked.connect(self.Create_zpl)
        self.ui.reset_btn.clicked.connect(self.Reset)
        self.ui.Default_btn.clicked.connect(self.Input)
        self.ui.set_btn.clicked.connect(self.Setting)
        HelpAction = QAction("&Help", self.ui.menuBar())
        HelpAction.setShortcut('Ctrl+H')
        HelpAction.setStatusTip('Open Explain')
        HelpAction.triggered.connect(self.HelpCall)
        menuBar = self.ui.menuBar()
        fileMenu = menuBar.addMenu("&도움말")
        fileMenu.addAction(HelpAction)

        self.ui.show()

    def HelpCall(self):
        file = "./explain_GUI.txt"
        text = []
        with open(file, 'r', encoding='UTF8')as f:
            line = f.readlines()
            for lines in line:
                text.append(lines)
        #print('test')
        msg = QMessageBox()
        msg.setWindowTitle('GUI 사용설명서')
        msg.setText('\n'.join(text))
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    def Setting(self):
        x_value = self.ui.x_ln.text()
        y_value = self.ui.y_ln.text()
        code_value = self.ui.barcode_ln.text()
        ZPL= "^XA\n^LH" + x_value + "," + y_value + "\n^FO000,000\n^BY2^BC,100,Y,N,N,A\n^FD" + code_value + "^FS\n^PQ0001^FS\n^XZ"
        self.ui.ZPL_ln.setText(ZPL)

    def Input(self):
        self.ui.x_ln.setText("000")
        self.ui.y_ln.setText("000")
        self.ui.barcode_ln.setText("1234567890")
        self.ui.cnt_ln.setText("0001")

    def Reset(self):
        self.ui.ZPL_ln.clear()
        self.ui.x_ln.clear()
        self.ui.y_ln.clear()
        self.ui.barcode_ln.clear()
        self.ui.cnt_ln.clear()

    def Create_zpl(self):
        x_value = self.ui.x_ln.text()
        y_value = self.ui.y_ln.text()
        code_value = self.ui.barcode_ln.text()
        cnt_value = self.ui.cnt_ln.text()
        ZPL = "^XA\n^FO" + x_value + "," + y_value + "\n^BY2^BC,100,Y,N,N,A\n^FD" + code_value + "^FS\n^PQ"+cnt_value+"^FS\n^XZ"
        # Code128, 마지막 A 모드 매개변수를 붙여줌으로써 최상의 방법으로 바코드를 찍어줌.
        self.ui.ZPL_ln.setText(ZPL)

    def Go_to_ZD(self):
        subprocess.Popen(ZD_dir)

    def Go_to_ZSU(self):
        app = Application().start(ZSU_dir)
        app.ZebraSetupUtilities.프린터와의통신열기.click()
        app.직접통신ZDesignerGT800.제목없음1.Edit.set_edit_text(self.ui.ZPL_ln.toPlainText())
        time.sleep(0.7)
        app.직접통신ZDesignerGT800.click_input(coords=(555, 60))
