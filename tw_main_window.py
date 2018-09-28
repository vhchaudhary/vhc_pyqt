# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tw_test.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtname = QtWidgets.QLineEdit(self.centralwidget)
        self.txtname.setGeometry(QtCore.QRect(172, 40, 181, 25))
        self.txtname.setObjectName("txtname")
        self.txtcity = QtWidgets.QLineEdit(self.centralwidget)
        self.txtcity.setGeometry(QtCore.QRect(172, 110, 181, 25))
        self.txtcity.setObjectName("txtcity")
        self.btninsert = QtWidgets.QPushButton(self.centralwidget)
        self.btninsert.setGeometry(QtCore.QRect(390, 170, 89, 25))
        self.btninsert.setObjectName("btninsert")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 40, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 110, 67, 17))
        self.label_2.setObjectName("label_2")
        self.tw_display = QtWidgets.QTableWidget(self.centralwidget)
        self.tw_display.setGeometry(QtCore.QRect(120, 260, 331, 191))
        self.tw_display.setObjectName("tw_display")
        self.tw_display.setColumnCount(3)
        self.tw_display.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_display.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_display.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_display.setHorizontalHeaderItem(2, item)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 170, 67, 17))
        self.label_3.setObjectName("label_3")
        self.radioMale = QtWidgets.QRadioButton(self.centralwidget)
        self.radioMale.setGeometry(QtCore.QRect(180, 170, 112, 23))
        self.radioMale.setObjectName("radioMale")
        self.radioMale.setChecked(True)
        self.radioFemale = QtWidgets.QRadioButton(self.centralwidget)
        self.radioFemale.setGeometry(QtCore.QRect(260, 170, 112, 23))
        self.radioFemale.setObjectName("radioFemale")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btninsert.setText(_translate("MainWindow", "Insert"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_2.setText(_translate("MainWindow", "City"))
        item = self.tw_display.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tw_display.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "City"))
        item = self.tw_display.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Gender"))
        self.label_3.setText(_translate("MainWindow", "Gender"))
        self.radioMale.setText(_translate("MainWindow", "Male"))
        self.radioFemale.setText(_translate("MainWindow", "Female"))

