# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'otto_dialog.ui'
#
# Created: Sat Aug 31 19:28:13 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Otto_dialog(object):
    def setupUi(self, Otto_dialog):
        Otto_dialog.setObjectName(_fromUtf8("Otto_dialog"))
        Otto_dialog.resize(400, 336)
        self.templab = QtGui.QLabel(Otto_dialog)
        self.templab.setGeometry(QtCore.QRect(40, 30, 151, 21))
        self.templab.setObjectName(_fromUtf8("templab"))
        self.preslab = QtGui.QLabel(Otto_dialog)
        self.preslab.setGeometry(QtCore.QRect(40, 80, 141, 31))
        self.preslab.setObjectName(_fromUtf8("preslab"))
        self.crat = QtGui.QLabel(Otto_dialog)
        self.crat.setGeometry(QtCore.QRect(40, 150, 131, 21))
        self.crat.setObjectName(_fromUtf8("crat"))
        self.anylab = QtGui.QLabel(Otto_dialog)
        self.anylab.setGeometry(QtCore.QRect(40, 220, 151, 21))
        self.anylab.setObjectName(_fromUtf8("anylab"))
        self.temped = QtGui.QLineEdit(Otto_dialog)
        self.temped.setGeometry(QtCore.QRect(230, 30, 113, 31))
        self.temped.setObjectName(_fromUtf8("temped"))
        self.presed = QtGui.QLineEdit(Otto_dialog)
        self.presed.setGeometry(QtCore.QRect(230, 80, 113, 31))
        self.presed.setObjectName(_fromUtf8("presed"))
        self.credit = QtGui.QLineEdit(Otto_dialog)
        self.credit.setGeometry(QtCore.QRect(230, 150, 113, 31))
        self.credit.setObjectName(_fromUtf8("credit"))
        self.combo = QtGui.QComboBox(Otto_dialog)
        self.combo.setGeometry(QtCore.QRect(230, 220, 111, 31))
        self.combo.setObjectName(_fromUtf8("combo"))
        self.combo.addItem(_fromUtf8(""))
        self.combo.addItem(_fromUtf8(""))
        self.combo.addItem(_fromUtf8(""))
        self.anyed = QtGui.QLineEdit(Otto_dialog)
        self.anyed.setGeometry(QtCore.QRect(230, 220, 111, 31))
        self.anyed.setObjectName(_fromUtf8("anyed"))
        self.anyed.hide()
        self.simulate = QtGui.QPushButton(Otto_dialog)
        self.simulate.setGeometry(QtCore.QRect(160, 280, 95, 31))
        self.simulate.setObjectName(_fromUtf8("simulate"))

        self.retranslateUi(Otto_dialog)
        QtCore.QObject.connect(self.combo, QtCore.SIGNAL(_fromUtf8("activated(int)")), self.combo.close)
        QtCore.QMetaObject.connectSlotsByName(Otto_dialog)

    def retranslateUi(self, Otto_dialog):
        Otto_dialog.setWindowTitle(QtGui.QApplication.translate("Otto_dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.templab.setText(QtGui.QApplication.translate("Otto_dialog", "Enter temperature (K)", None, QtGui.QApplication.UnicodeUTF8))
        self.preslab.setText(QtGui.QApplication.translate("Otto_dialog", "Enter pressure (KPa)", None, QtGui.QApplication.UnicodeUTF8))
        self.crat.setText(QtGui.QApplication.translate("Otto_dialog", "Compression Ratio", None, QtGui.QApplication.UnicodeUTF8))
        self.anylab.setText(QtGui.QApplication.translate("Otto_dialog", "Enter any one of these", None, QtGui.QApplication.UnicodeUTF8))
        self.combo.setItemText(0, QtGui.QApplication.translate("Otto_dialog", "Max Temp (K)", None, QtGui.QApplication.UnicodeUTF8))
        self.combo.setItemText(1, QtGui.QApplication.translate("Otto_dialog", "Max Pressure(KPa)", None, QtGui.QApplication.UnicodeUTF8))
        self.combo.setItemText(2, QtGui.QApplication.translate("Otto_dialog", "Heat at constant vol (KJ)", None, QtGui.QApplication.UnicodeUTF8))
        self.simulate.setText(QtGui.QApplication.translate("Otto_dialog", "Simulate", None, QtGui.QApplication.UnicodeUTF8))

