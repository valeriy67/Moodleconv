# -*- coding: utf-8 -*-

__author__ = 'gbrva'

import logging
import os
import sys
import traceback

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

from convert import *
from interface import *

# Номер збірки
numBuild = '02_230903'
logger = logging.getLogger('convert')
hdlr = logging.FileHandler('converter.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)
class MyWin(QtWidgets.QMainWindow):
    mdlFlag = True

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowIcon(QIcon('main.ico'))
        self.ui = Ui_Main()
        self.ui.setupUi(self)


        # Встановлюємо початкові значення
        self.ui.pushButton.setEnabled(False)
        self.ui.progressBar.setProperty('value', 0)

        # Приєднуємо слоти
        self.ui.pushButton.clicked.connect(self.do_convert)
        self.ui.toolButton.clicked.connect(self.do_selectfile)
        self.ui.MoodleBtn.clicked.connect(self.do_moodleClick)
        self.ui.TextBtn.clicked.connect(self.do_textClick)

    def do_moodleClick(self):
        self.ui.MoodleBox.setChecked(True)
        self.ui.FotoBox.setChecked(False)
        self.ui.FotoBox.setEnabled(True)
        self.ui.GoogleBox.setChecked(False)
        return None

    def do_textClick(self):
        self.ui.MoodleBox.setChecked(True)
        self.ui.FotoBox.setChecked(False)
        self.ui.FotoBox.setEnabled(False)
        self.ui.GoogleBox.setChecked(False)

        pass

    def do_selectfile(self):
        fname = QtWidgets.QFileDialog.getOpenFileName()[0]
        self.ui.lineEdit.setText(str(fname))
        if fname != '':
            self.ui.pushButton.setEnabled(True)
        return None

    def do_convert(self):
        try:
            frname = self.ui.lineEdit.text()
            tmpname = os.path.split(frname)
            tmp_name_short=os.path.splitext(tmpname[1])
            fwname = os.path.join(tmpname[0], 'mdl_' + tmp_name_short[0]+'.csv')
            text1 = self.ui.outlabel.setText('Output file: ' + fwname)
            if self.ui.MoodleBtn.isChecked():
                Convert_1c(frname, fwname, self.ui.FotoBox.isChecked())
            else:
                Convert_Text(frname, fwname)
            # self.ui.progressBar.setProperty('value', newvalue)
            self.ui.lineEdit.setText('')
            self.ui.pushButton.setEnabled(False)
        except Exception as e:  # work on python 3.x
            logger.exception (e)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Convert failed! See log for details')
            msg.setWindowTitle("Error")
            msg.exec_()
        return None


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
