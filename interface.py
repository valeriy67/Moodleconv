# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'moodle_gui.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(400, 400)
        Main.setMaximumSize(QtCore.QSize(400, 400))
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MoodleBtn = QtWidgets.QRadioButton(self.groupBox)
        self.MoodleBtn.setCheckable(True)
        self.MoodleBtn.setChecked(True)
        self.MoodleBtn.setObjectName("MoodleBtn")
        self.verticalLayout.addWidget(self.MoodleBtn)
        self.TextBtn = QtWidgets.QRadioButton(self.groupBox)
        self.TextBtn.setObjectName("TextBtn")
        self.verticalLayout.addWidget(self.TextBtn)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.MoodleBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.MoodleBox.setChecked(True)
        self.MoodleBox.setObjectName("MoodleBox")
        self.verticalLayout_2.addWidget(self.MoodleBox)
        self.FotoBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.FotoBox.setObjectName("FotoBox")
        self.verticalLayout_2.addWidget(self.FotoBox)
        self.GoogleBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.GoogleBox.setObjectName("GoogleBox")
        self.verticalLayout_2.addWidget(self.GoogleBox)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.outlabel = QtWidgets.QLabel(self.centralwidget)
        self.outlabel.setObjectName("outlabel")
        self.verticalLayout_3.addWidget(self.outlabel)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(382, 0))
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        Main.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(Main)
        self.statusBar.setObjectName("statusBar")
        Main.setStatusBar(self.statusBar)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "1C to Moodle"))
        self.label_2.setText(_translate("Main", "1С в  MOODLE"))
        self.label.setText(_translate("Main", "Оберіть файл"))
        self.toolButton.setText(_translate("Main", "..."))
        self.groupBox.setTitle(_translate("Main", "Вхідний файл"))
        self.MoodleBtn.setText(_translate("Main", "1С -MOODLE"))
        self.TextBtn.setText(_translate("Main", "Текстовий файл"))
        self.groupBox_2.setTitle(_translate("Main", "Вихідні файли"))
        self.MoodleBox.setText(_translate("Main", "Імпорт в Moodle"))
        self.FotoBox.setText(_translate("Main", "Додати фотографії"))
        self.GoogleBox.setText(_translate("Main", "Імпорт в Google Apss"))
        self.outlabel.setText(_translate("Main", "Шлях запису файлів"))
        self.pushButton.setText(_translate("Main", "Виконати"))

