from PyQt4 import QtGui, QtCore
import os, sys
import pylab
import numpy

from auto_main import Ui_thermo
from auto_otto import Ui_Otto_dialog
from auto_dual import Ui_Dialog

R = 0.287
gamma = 1.4
cv = 0.718
cp = 1.005

def checkFloat(number):
    r"""
    Checks if a given number is float or not. If it is, it returns the
    number.
    """
    try:
        number = float(number)
    except ValueError, e:
        return False
    else:
        return float(number)

class Main(QtGui.QMainWindow):
    r"""
    Class for the main window
    """
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_thermo()
        self.ui.setupUi(self)
        self.ui.otto_button.clicked.connect(self.otto_window)
        self.ui.diesel_button.clicked.connect(self.diesel_window)
        self.ui.dual_button.clicked.connect(self.dual_window)

    def otto_window(self):
        otto = odialog()
        otto.exec_()

    def diesel_window(self):
        diesel = ddialog()
        diesel.exec_()

    def dual_window(self):
        dual = dudialog()
        dual.exec_()

class odialog(QtGui.QDialog):
    r"""
    Class for the Otto Dialog window
    """
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.press = 0
        self.ui = Ui_Otto_dialog()
        self.ui.setupUi(self)
        self.ui.combo.activated.connect(self.change)
        self.ui.simulate.clicked.connect(self.simulate)  # Push Button

    def simulate(self):
        temp = checkFloat(self.ui.temped.text())
        pres = checkFloat(self.ui.presed.text())
        cr = checkFloat(self.ui.credit.text())
        any_ = checkFloat(self.ui.anyed.text())

        if all([temp, pres, cr, any_]):
            self.cr = cr
            self.T1 = temp
            self.P1 = pres
            self.v1 = (R*self.T1)/self.P1
            self.P2 = self.P1*pow(cr, gamma)
            self.v2 = self.v1/cr
            self.T2 = self.T1*pow(cr, gamma - 1)
            self.v3 = self.v2
            self.v4 = self.v1
            self.any = any_
            self.gascalc()


        elif not self.press:
            msgbox = QtGui.QMessageBox.warning(self, "Warning",
                "Enter valid input", QtGui.QMessageBox.Ok)

    def gascalc(self):
        self.press = 1
        if self.text == 1:
            self.P3 = self.any
            self.T3 = self.P3*(self.T2/self.P2)
        elif self.text == 2:
            self.T3 = (self.any/cv) + self.T2
            self.P3 = self.T3*(self.P2/self.T2)
        else:
            self.T3 = self.any
            self.P3 = self.T3*(self.P2/self.T2)
        self.heat = cv*(self.T3 - self.T2)
        self.P4 = pow((self.v3/self.v4), gamma)*self.P3
        self.T4 = self.T3*pow(1/self.cr, gamma - 1)
        self.eff = 1 - (1/pow(self.cr, gamma - 1))
        self.work = self.heat*self.eff
        self.finalGUI()

    def finalGUI(self):
        self.ui.templab.setText("Heat supplied")
        self.ui.templab.adjustSize()
        self.ui.temped.setText(str(self.heat))
        self.ui.temped.adjustSize()
        self.ui.temped.setReadOnly(True)
        self.ui.preslab.setText("Work done")
        self.ui.preslab.adjustSize()
        self.ui.presed.setText(str(self.work))
        self.ui.presed.adjustSize()
        self.ui.presed.setReadOnly(True)
        self.ui.crat.setText("Max Pres / Temp")
        self.ui.crat.adjustSize()
        self.ui.credit.setText(str(self.P3) + "|" + str(self.T3))
        self.ui.credit.adjustSize()
        self.ui.credit.setReadOnly(True)
        self.ui.anylab.setText("Efficiency")
        self.ui.anylab.adjustSize()
        self.ui.anyed.setText(str(self.eff))
        self.ui.anyed.adjustSize()
        self.ui.anyed.setReadOnly(True)
        self.ui.simulate.setText("Plot")
        self.ui.simulate.clicked.connect(self.reject)

    def reject(self):
        super(odialog, self).reject()
        constant1 = self.P2*pow(self.v2, gamma)
        constant2 = self.P4*pow(self.v1, gamma)
        x1 = numpy.linspace(self.v1, self.v2, 100)
        y1 = constant1*pow(x1, -gamma)
        pylab.plot(x1, y1)
        x2 = numpy.linspace(self.v2, self.v3, 100)
        y2 = numpy.linspace(self.P2, self.P3, 100)
        pylab.plot(x2, y2)
        x3 = numpy.linspace(self.v3, self.v1, 100)
        y3 = constant2*pow(x3, -gamma)
        pylab.plot(x3, y3)
        x4 = numpy.linspace(self.v1, self.v1, 100)
        y4 = numpy.linspace(self.P4, self.P1, 100)
        pylab.plot(x4, y4)
        pylab.show()
        

    def change(self, text):
        list_ = ["max temp(K)", "max press(KPa)", "heat at constant vol"]
        self.ui.anylab.setText("Enter " + list_[text])
        self.ui.anylab.adjustSize()
        self.ui.anyed.show()
        self.text = text

class ddialog(odialog):
    def __init__(self):
        super(ddialog, self).__init__()
        self.ui.combo.removeItem(1)
        self.ui.combo.removeItem(1)
        self.ui.combo.addItem("Heat at constant P")

    def simulate(self):
        temp = checkFloat(self.ui.temped.text())
        pres = checkFloat(self.ui.presed.text())
        cr = checkFloat(self.ui.credit.text())
        any_ = checkFloat(self.ui.anyed.text())

        if all([temp, pres, cr, any_]):
            self.cr = cr
            self.T1 = temp
            self.P1 = pres
            self.v1 = (R*self.T1)/self.P1
            self.P2 = self.P1*pow(cr, gamma)
            self.v2 = self.v1/cr
            self.T2 = self.T1*pow(cr, gamma - 1)
            self.P3 = self.P2
            self.v4 = self.v1
            self.any = any_
            self.gascalc()

        elif not self.press:
            msgbox = QtGui.QMessageBox.warning(self, "Warning",
                "Enter valid input", QtGui.QMessageBox.Ok)

    def gascalc(self):
        self.press = 1
        if self.text == 1:
            self.T3 = (self.any/cp) + self.T2
        else:
            self.T3 = self.any
        self.v3 = (R*self.T3)/self.P3
        self.heat = cp*(self.T3 - self.T2)
        self.P4 = pow((self.v3/self.v4), gamma)*self.P3
        self.T4 = self.T3*pow((self.cr/(self.T3/self.T2)), 1 - gamma)
        self.eff = 1 - (self.T4 - self.T1)/(gamma*(self.T3 - self.T2))
        self.work = self.heat*self.eff
        self.finalGUI()


class dudialog(QtGui.QDialog):
    r"""
    Class for the Dual Dialog window
    """
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.press = 0
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.any1c.activated.connect(self.change1)
        self.ui.simulate.clicked.connect(self.simulate)


    def simulate(self):
        temp = checkFloat(self.ui.temped.text())
        pres = checkFloat(self.ui.presed.text())
        cr = checkFloat(self.ui.credit.text())
        any1 = checkFloat(self.ui.any1ed.text())
        any2 = checkFloat(self.ui.any2ed.text())

        if all([temp, pres, cr, any1, any2]):
            self.cr = cr
            self.T1 = temp
            self.P1 = pres
            self.v1 = (R*self.T1)/self.P1
            self.P2 = self.P1*pow(cr, gamma)
            self.v2 = self.v1/cr
            self.T2 = self.T1*pow(cr, gamma - 1)
            self.v3 = self.v2
            self.v5 = self.v1
            self.any1 = any1
            self.any2 = any2
            self.gascalc()

        elif not self.press:
            msgbox = QtGui.QMessageBox.warning(self, "Warning",
                "Enter valid input", QtGui.QMessageBox.Ok)

    def gascalc(self):
        self.press = 1
        if not self.text1:
            # self.any1 gives max Pressure
            # self.any2 gives heat at constant Pressure
            self.P3 = self.any1
            self.P4 = self.P3
            self.T3 = self.P3*(self.T2/self.P2)
            self.T4 = self.T3 + self.any2/cp

        else:
            # self.any1 gives max temp
            self.T4 = self.any1
            if not self.text2:
                # self.any2 gives heat at constant P
                self.T3 = self.T4 - self.any2/cp
            else:
                # self.any2 gives heat at constant v
                self.T3 = self.T2 + self.any2/cv
            self.P3 = self.T3*(self.P2*self.T2)
            self.P4 = self.P3

        self.v4 = self.T4*(self.v3/self.T3)
        self.P5 = self.P4*pow((self.v4/self.v5), gamma)
        self.T5 = self.T4*pow((self.v4/self.v5), gamma - 1)
        self.h1 = cv*(self.T3 - self.T2)
        self.h2 = cp*(self.T4 - self.T3)
        self.heat = self.h1 + self.h2
        self.eff = 1 - (self.T5 - self.T1)/(self.T3 - self.T2 + gamma*(
            self.T4 - self.T3))
        self.work = self.heat*self.eff
        self.finalGUI()

    def change1(self, text):
        self.text1 = text
        list_ = ["max press (kPa)", "max temp(K)"]
        self.ui.e1lab.setText("Enter " + list_[text])
        self.ui.any1ed.show()
        if not text:  # Pressure
            self.ui.e2lab.setText("Heat at constant P")
            self.ui.any2ed.show()
        else:
            self.ui.e2lab.setText("Enter any one")
            self.ui.any2c.addItem("Heat at constant v")
            self.ui.any2c.show()
            self.ui.any2c.activated.connect(self.change2)

    def change2(self, text):
        self.text2 = text
        list_ = ["heat at constant P", "heat at constant v"]
        self.ui.e2lab.setText("Enter " + list_[text])
        self.ui.any2ed.show()

    def finalGUI(self):
        self.ui.templab.setText("Heat supplied at constant vol")
        self.ui.templab.adjustSize()
        self.ui.temped.setText(str(self.h1))
        self.ui.temped.adjustSize()
        self.ui.temped.setReadOnly(True)
        self.ui.preslab.setText("Heat supplied at constant P")
        self.ui.preslab.adjustSize()
        self.ui.presed.setText(str(self.h2))
        self.ui.presed.adjustSize()
        self.ui.presed.setReadOnly(True)
        self.ui.cred.setText("Work Done")
        self.ui.cred.adjustSize()
        self.ui.credit.setText(str(self.work))
        self.ui.credit.adjustSize()
        self.ui.credit.setReadOnly(True)
        self.ui.e2lab.setText("Efficiency")
        self.ui.e2lab.adjustSize()
        self.ui.any2ed.setText(str(self.eff))
        self.ui.any2ed.adjustSize()
        self.ui.any2ed.setReadOnly(True)
        self.ui.e1lab.setText("Max P | T")
        self.ui.e1lab.adjustSize()
        self.ui.any1ed.setText(str(self.P4) + "|" + str(self.T4))
        self.ui.any1ed.adjustSize()
        self.ui.any1ed.setReadOnly(True)
        self.ui.simulate.setText("Plot")
        self.ui.simulate.clicked.connect(self.reject)

    def reject(self):
        super(dudialog, self).reject()
        constant1 = self.P2*pow(self.v2, gamma)
        constant2 = self.P5*pow(self.v5, gamma)
        x1 = numpy.linspace(self.v1, self.v2, 100)
        y1 = constant1*pow(x1, -gamma)
        pylab.plot(x1, y1)
        x2 = numpy.linspace(self.v2, self.v3, 100)
        y2 = numpy.linspace(self.P2, self.P3, 100)
        pylab.plot(x2, y2)
        x3 = numpy.linspace(self.v3, self.v4, 100)
        y3 = numpy.linspace(self.P3, self.P4, 100)
        pylab.plot(x3, y3)
        x4 = numpy.linspace(self.v4, self.v5, 100)
        y4 = constant2*pow(x4, -gamma)
        pylab.plot(x4, y4)
        x5 = numpy.linspace(self.v5, self.v1, 100)
        y5 = numpy.linspace(self.P5, self.P1, 100)
        pylab.plot(x5, y5)
        pylab.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ther = Main()
    ther.show()
    sys.exit(app.exec_())
