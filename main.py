# -*- coding: utf-8 -*-

__author__ = 'gbrva'

from convert import *
from interface import *
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

# Номер збірки
numBuild = '01_210915'


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
        frname = self.ui.lineEdit.text()
        tmpname = os.path.split(frname)
        fwname = os.path.join(tmpname[0], 'mdl_' + tmpname[1])
        text1 = self.ui.outlabel.setText('Output file: ' + fwname)
        if self.ui.MoodleBtn.isChecked():
            Convert_1c(frname, fwname, self.ui.FotoBox.isChecked())
        else:
            Convert_Text(frname, fwname)
        # self.ui.progressBar.setProperty('value', newvalue)
        self.ui.lineEdit.setText('')
        self.ui.pushButton.setEnabled(False)
        return None


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
