# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'auto_dual.ui'
#
# Created: Sun Sep  1 11:03:16 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(469, 404)
        self.temped = QtGui.QLineEdit(Dialog)
        self.temped.setGeometry(QtCore.QRect(280, 30, 113, 31))
        self.temped.setObjectName(_fromUtf8("temped"))
        self.presed = QtGui.QLineEdit(Dialog)
        self.presed.setGeometry(QtCore.QRect(280, 90, 113, 31))
        self.presed.setObjectName(_fromUtf8("presed"))
        self.credit = QtGui.QLineEdit(Dialog)
        self.credit.setGeometry(QtCore.QRect(280, 150, 113, 31))
        self.credit.setObjectName(_fromUtf8("credit"))
        self.any1c = QtGui.QComboBox(Dialog)
        self.any1c.setGeometry(QtCore.QRect(280, 220, 78, 31))
        self.any1c.setObjectName(_fromUtf8("any1c"))
        self.any1c.addItem(_fromUtf8(""))
        self.any1c.addItem(_fromUtf8(""))
        self.any1ed = QtGui.QLineEdit(Dialog)
        self.any1ed.setGeometry(QtCore.QRect(280, 220, 78, 31))
        self.any1ed.setObjectName(_fromUtf8("any1ed"))
        self.any1ed.hide()
        self.any2c = QtGui.QComboBox(Dialog)
        self.any2c.setGeometry(QtCore.QRect(280, 280, 78, 31))
        self.any2c.setObjectName(_fromUtf8("any2c"))
        self.any2c.hide()
        self.any2ed = QtGui.QLineEdit(Dialog)
        self.any2ed.setGeometry(QtCore.QRect(280, 280, 78, 31))
        self.any2ed.setObjectName(_fromUtf8("any2ced"))
        self.any2ed.hide()
        self.any2c.addItem(_fromUtf8(""))
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 160, 301))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.templab = QtGui.QLabel(self.verticalLayoutWidget)
        self.templab.setObjectName(_fromUtf8("templab"))
        self.verticalLayout.addWidget(self.templab)
        self.preslab = QtGui.QLabel(self.verticalLayoutWidget)
        self.preslab.setObjectName(_fromUtf8("preslab"))
        self.verticalLayout.addWidget(self.preslab)
        self.cred = QtGui.QLabel(self.verticalLayoutWidget)
        self.cred.setObjectName(_fromUtf8("cred"))
        self.verticalLayout.addWidget(self.cred)
        self.e1lab = QtGui.QLabel(self.verticalLayoutWidget)
        self.e1lab.setObjectName(_fromUtf8("e1lab"))
        self.verticalLayout.addWidget(self.e1lab)
        self.e2lab = QtGui.QLabel(self.verticalLayoutWidget)
        self.e2lab.setObjectName(_fromUtf8("e2lab"))
        self.verticalLayout.addWidget(self.e2lab)
        self.simulate = QtGui.QPushButton(Dialog)
        self.simulate.setGeometry(QtCore.QRect(190, 340, 95, 31))
        self.simulate.setObjectName(_fromUtf8("simulate"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.any1c.setItemText(0, QtGui.QApplication.translate("Dialog", "Max Pressure (KPa)", None, QtGui.QApplication.UnicodeUTF8))
        self.any1c.setItemText(1, QtGui.QApplication.translate("Dialog", "Max Temp (K)", None, QtGui.QApplication.UnicodeUTF8))
        self.any2c.setItemText(0, QtGui.QApplication.translate("Dialog", "Heat at constant pres", None, QtGui.QApplication.UnicodeUTF8))
        self.templab.setText(QtGui.QApplication.translate("Dialog", "Enter temperature(K)", None, QtGui.QApplication.UnicodeUTF8))
        self.preslab.setText(QtGui.QApplication.translate("Dialog", "Enter pressure (KPa)", None, QtGui.QApplication.UnicodeUTF8))
        self.cred.setText(QtGui.QApplication.translate("Dialog", "Compression Ratio", None, QtGui.QApplication.UnicodeUTF8))
        self.e1lab.setText(QtGui.QApplication.translate("Dialog", "Enter one of these", None, QtGui.QApplication.UnicodeUTF8))
        self.simulate.setText(QtGui.QApplication.translate("Dialog", "Simulate", None, QtGui.QApplication.UnicodeUTF8))

