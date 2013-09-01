# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ThermoPython.ui'
#
# Created: Sat Aug 31 15:10:33 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_thermo(object):
    def setupUi(self, thermo):
        thermo.setObjectName(_fromUtf8("thermo"))
        thermo.resize(552, 500)
        self.centralwidget = QtGui.QWidget(thermo)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(200, 10, 160, 401))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.vlayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.vlayout.setMargin(0)
        self.vlayout.setObjectName(_fromUtf8("vlayout"))
        self.otto_button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.otto_button.setObjectName(_fromUtf8("otto_button"))
        self.vlayout.addWidget(self.otto_button)
        self.diesel_button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.diesel_button.setObjectName(_fromUtf8("diesel_button"))
        self.vlayout.addWidget(self.diesel_button)
        self.dual_button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.dual_button.setObjectName(_fromUtf8("dual_button"))
        self.vlayout.addWidget(self.dual_button)
        thermo.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(thermo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 552, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        thermo.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(thermo)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        thermo.setStatusBar(self.statusbar)

        self.retranslateUi(thermo)
        QtCore.QMetaObject.connectSlotsByName(thermo)

    def retranslateUi(self, thermo):
        thermo.setWindowTitle(QtGui.QApplication.translate("thermo", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.otto_button.setText(QtGui.QApplication.translate("thermo", "Otto", None, QtGui.QApplication.UnicodeUTF8))
        self.diesel_button.setText(QtGui.QApplication.translate("thermo", "Diesel", None, QtGui.QApplication.UnicodeUTF8))
        self.dual_button.setText(QtGui.QApplication.translate("thermo", "Dual", None, QtGui.QApplication.UnicodeUTF8))

