#!/usr/bin/python
 
import sys
from CutUtilQt import *
from PyQt4 import QtGui

class CutMainWindow(QtGui.QMainWindow):

	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setWindowTitle("Count Up Timer")
		self.setCentralWidget(CutUtilQt.getContainerWidget())
		self.show()


application = QtGui.QApplication(sys.argv)
cutMainWindow = CutMainWindow()
application.exec_()
