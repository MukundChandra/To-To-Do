# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import os
import random
import re

def Collect_Text_Files():
      ListOfTextFiles = []
      try:
            os.mkdir("TextFiles")
      except FileExistsError:
            pass
      os.chdir("TextFiles")
      for item in os.listdir():
            if re.match("(_| |[0-9a-zA-Z])*.txt",item):
                  X = open(item,"r")
                  Y = X.read()
                  ListOfTextFiles.append(Y)
      return ListOfTextFiles

TextList = Collect_Text_Files()
ui = None

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.counter = 0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 240)
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.P1 = QtWidgets.QPushButton(self.centralwidget)
        self.P1.setObjectName("P1")
        self.horizontalLayout.addWidget(self.P1)
        self.P2 = QtWidgets.QPushButton(self.centralwidget)
        self.P2.setObjectName("P2")
        self.horizontalLayout.addWidget(self.P2)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ToToDo 1.0"))
        self.label.setText(_translate("MainWindow", "Welcome to ToToDo!"))
        self.P1.setText(_translate("MainWindow", "<"))
        self.P2.setText(_translate("MainWindow", ">"))
        try:
              self.P1.clicked.connect(B1_Click)
              self.P2.clicked.connect(B2_Click)
        except Exception as c:
              print(c)

def B1_Click():
      _translate = QtCore.QCoreApplication.translate
      if len(TextList) > 0:
            ui.counter -= 1
            ui.counter %= len(TextList)
            if ui.counter < 0:
                  ui.counter *= -1
            ui.label.setText(_translate("MainWindow", TextList[ui.counter]))
        
def B2_Click():
      _translate = QtCore.QCoreApplication.translate
      if len(TextList) > 0:
            ui.counter += 1
            ui.counter %= len(TextList)
            ui.label.setText(_translate("MainWindow", TextList[ui.counter]))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

