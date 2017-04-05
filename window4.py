# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window4.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import lightstyle

class Ui_window4(object):
    def setupUi(self, window4):
        window4.setObjectName("window4")
        window4.resize(920, 469)
        window4.setStyleSheet(lightstyle.css)
        window4.setWindowIcon(QtGui.QIcon('icons/favicon.ico'))
        self.centralwidget = QtWidgets.QWidget(window4)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.faculty_combobox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.faculty_combobox.sizePolicy().hasHeightForWidth())
        self.faculty_combobox.setSizePolicy(sizePolicy)
        self.faculty_combobox.setMinimumSize(QtCore.QSize(305, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.faculty_combobox.setFont(font)
        self.faculty_combobox.setObjectName("faculty_combobox")
        self.gridLayout.addWidget(self.faculty_combobox, 1, 1, 1, 1)
        self.faculty_table = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.faculty_table.sizePolicy().hasHeightForWidth())
        self.faculty_table.setSizePolicy(sizePolicy)
        self.faculty_table.setMinimumSize(QtCore.QSize(596, 290))
        self.faculty_table.setObjectName("faculty_table")
        self.faculty_table.setColumnCount(8)
        self.faculty_table.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.faculty_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.faculty_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.faculty_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.faculty_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.faculty_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.faculty_table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.faculty_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.faculty_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.faculty_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.faculty_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.faculty_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.faculty_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.faculty_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.faculty_table.setHorizontalHeaderItem(7, item)
        self.faculty_table.horizontalHeader().setDefaultSectionSize(100)
        self.faculty_table.horizontalHeader().setMinimumSectionSize(37)
        self.faculty_table.verticalHeader().setDefaultSectionSize(43)
        self.faculty_table.verticalHeader().setMinimumSectionSize(27)
        self.gridLayout.addWidget(self.faculty_table, 2, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 48))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 3, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.printBtn = QtWidgets.QPushButton(self.centralwidget)
        self.printBtn.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.printBtn.setFont(font)
        self.printBtn.setObjectName("printBtn")
        self.horizontalLayout.addWidget(self.printBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.backBtn.setFont(font)
        self.backBtn.setObjectName("backBtn")
        self.horizontalLayout.addWidget(self.backBtn)
        self.generateBtn = QtWidgets.QPushButton(self.centralwidget)
        self.generateBtn.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.generateBtn.setFont(font)
        self.generateBtn.setObjectName("generateBtn")
        self.horizontalLayout.addWidget(self.generateBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        window4.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window4)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        window4.setMenuBar(self.menubar)
        self.actionSave = QtWidgets.QAction(window4)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.setShortcut("Ctrl+S")
        self.actionLoad = QtWidgets.QAction(window4)
        self.actionLoad.setObjectName("actionLoad")
        self.actionLoad.setShortcut("Ctrl+L")
        self.actionExit = QtWidgets.QAction(window4)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(window4)
        self.actionAbout.setObjectName("actionAbout")
        self.actionManual = QtWidgets.QAction(window4)
        self.actionManual.setObjectName("actionManual")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionManual)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(window4)
        QtCore.QMetaObject.connectSlotsByName(window4)
        window4.setTabOrder(self.faculty_combobox, self.faculty_table)
        window4.setTabOrder(self.faculty_table, self.printBtn)
        window4.setTabOrder(self.printBtn, self.backBtn)
        window4.setTabOrder(self.backBtn, self.generateBtn)

    def retranslateUi(self, window4):
        _translate = QtCore.QCoreApplication.translate
        window4.setWindowTitle(_translate("window4", "TimeTable Generator"))
        self.label_2.setText(_translate("window4", "Faculty:"))
        item = self.faculty_table.verticalHeaderItem(0)
        item.setText(_translate("window4", "Monday"))
        item = self.faculty_table.verticalHeaderItem(1)
        item.setText(_translate("window4", "Tuesday"))
        item = self.faculty_table.verticalHeaderItem(2)
        item.setText(_translate("window4", "Wednesday"))
        item = self.faculty_table.verticalHeaderItem(3)
        item.setText(_translate("window4", "Thursday"))
        item = self.faculty_table.verticalHeaderItem(4)
        item.setText(_translate("window4", "Friday"))
        item = self.faculty_table.verticalHeaderItem(5)
        item.setText(_translate("window4", "Saturday"))
        item = self.faculty_table.horizontalHeaderItem(0)
        item.setText(_translate("window4", "9:00-9:55"))
        item = self.faculty_table.horizontalHeaderItem(1)
        item.setText(_translate("window4", "9:55-10:50"))
        item = self.faculty_table.horizontalHeaderItem(2)
        item.setText(_translate("window4", "11:10-12:05"))
        item = self.faculty_table.horizontalHeaderItem(3)
        item.setText(_translate("window4", "12:05-1:00"))
        item = self.faculty_table.horizontalHeaderItem(4)
        item.setText(_translate("window4", "1:00-1:55"))
        item = self.faculty_table.horizontalHeaderItem(5)
        item.setText(_translate("window4", "1:55-2:50"))
        item = self.faculty_table.horizontalHeaderItem(6)
        item.setText(_translate("window4", "2:50-3:40"))
        item = self.faculty_table.horizontalHeaderItem(7)
        item.setText(_translate("window4", "3:40-4:30"))
        self.label.setText(_translate("window4", "Faculty Constraints"))
        self.printBtn.setText(_translate("window4", "Print"))
        self.backBtn.setText(_translate("window4", "< Back"))
        self.generateBtn.setText(_translate("window4", "Generate >"))
        self.menuFile.setTitle(_translate("window4", "File"))
        self.menuHelp.setTitle(_translate("window4", "Help"))
        self.actionSave.setText(_translate("window4", "Save"))
        self.actionLoad.setText(_translate("window4", "Load"))
        self.actionExit.setText(_translate("window4", "Exit"))
        self.actionAbout.setText(_translate("window4", "About"))
        self.actionManual.setText(_translate("window4", "Manual"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window4 = QtWidgets.QMainWindow()
    ui = Ui_window4()
    ui.setupUi(window4)
    window4.show()
    sys.exit(app.exec_())

