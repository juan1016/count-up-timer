#!/usr/bin/python

from PyQt4 import QtGui
from PyQt4 import QtCore

class CutUtilQt:

	@staticmethod
	def getContainerWidget():
		containerWidget = QtGui.QWidget()
		containerWidget.setLayout(CutUtilQt.getContainerLayout())
		return containerWidget
	
	@staticmethod
	def getContainerLayout():
		containerLayout = QtGui.QVBoxLayout()
		containerLayout.addLayout(CutUtilQt.getTimeDisplay())
		containerLayout.addLayout(CutUtilQt.getControlWidgetsGroup())
		return containerLayout
	
	@staticmethod
	def getTimeDisplay():
		containerLayout = QtGui.QHBoxLayout()
		lcd = QtGui.QLCDNumber()
		lcd.setNumDigits(8)
		s = QtCore.QString('00:04:36')
		lcd.display(s)
		containerLayout.addWidget(lcd)
		return containerLayout
		
	@staticmethod
	def getControlWidgetsGroup():
		containerLayout = QtGui.QHBoxLayout()
		startButton = QtGui.QPushButton("Start")
		stopButton = QtGui.QPushButton("Stop")
		resetButton = QtGui.QPushButton("Reset")
		containerLayout.addWidget(startButton)
		containerLayout.addWidget(stopButton)
		containerLayout.addWidget(resetButton)
		return containerLayout
