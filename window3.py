# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window3.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import lightstyle
import darkstyle

class Ui_window3(object):
    def setupUi(self, window3):
        window3.setObjectName("window3")
        window3.resize(920, 469)
        window3.setStyleSheet(lightstyle.css)
        self.centralwidget = QtWidgets.QWidget(window3)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.semester_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.semester_combobox.setMinimumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.semester_combobox.setFont(font)
        self.semester_combobox.setObjectName("semester_combobox")
        self.gridLayout.addWidget(self.semester_combobox, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.section_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.section_combobox.setMinimumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.section_combobox.setFont(font)
        self.section_combobox.setObjectName("section_combobox")
        self.gridLayout.addWidget(self.section_combobox, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.subject_table = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subject_table.sizePolicy().hasHeightForWidth())
        self.subject_table.setSizePolicy(sizePolicy)
        self.subject_table.setMinimumSize(QtCore.QSize(596, 290))
        self.subject_table.setObjectName("subject_table")
        self.subject_table.setColumnCount(8)
        self.subject_table.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.subject_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.subject_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.subject_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.subject_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.subject_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.subject_table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.subject_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.subject_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.subject_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.subject_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.subject_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.subject_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.subject_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.subject_table.setHorizontalHeaderItem(7, item)
        self.subject_table.horizontalHeader().setDefaultSectionSize(100)
        self.subject_table.horizontalHeader().setMinimumSectionSize(37)
        self.subject_table.verticalHeader().setDefaultSectionSize(43)
        self.subject_table.verticalHeader().setMinimumSectionSize(27)
        self.gridLayout.addWidget(self.subject_table, 3, 0, 1, 4, QtCore.Qt.AlignVCenter)
        self.slotType_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.slotType_combobox.setMinimumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.slotType_combobox.setFont(font)
        self.slotType_combobox.setObjectName("slotType_combobox")
        self.gridLayout.addWidget(self.slotType_combobox, 2, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 25))
        self.label.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4, QtCore.Qt.AlignHCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 3, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.printBtn = QtWidgets.QPushButton(self.centralwidget)
        self.printBtn.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.printBtn.setFont(font)
        self.printBtn.setObjectName("printBtn")
        self.horizontalLayout.addWidget(self.printBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.backBtn.setFont(font)
        self.backBtn.setObjectName("backBtn")
        self.horizontalLayout.addWidget(self.backBtn)
        self.nextBtn = QtWidgets.QPushButton(self.centralwidget)
        self.nextBtn.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nextBtn.setFont(font)
        self.nextBtn.setObjectName("nextBtn")
        self.horizontalLayout.addWidget(self.nextBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        window3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        window3.setMenuBar(self.menubar)
        self.actionSave = QtWidgets.QAction(window3)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtWidgets.QAction(window3)
        self.actionLoad.setObjectName("actionLoad")
        self.actionExit = QtWidgets.QAction(window3)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(window3)
        self.actionAbout.setObjectName("actionAbout")
        self.actionManual = QtWidgets.QAction(window3)
        self.actionManual.setObjectName("actionManual")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionManual)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(window3)
        QtCore.QMetaObject.connectSlotsByName(window3)
        window3.setTabOrder(self.semester_combobox, self.section_combobox)
        window3.setTabOrder(self.section_combobox, self.slotType_combobox)
        window3.setTabOrder(self.slotType_combobox, self.subject_table)
        window3.setTabOrder(self.subject_table, self.printBtn)
        window3.setTabOrder(self.printBtn, self.backBtn)
        window3.setTabOrder(self.backBtn, self.nextBtn)

    def retranslateUi(self, window3):
        _translate = QtCore.QCoreApplication.translate
        window3.setWindowTitle(_translate("window3", "TimeTable Generator"))
        self.label_3.setText(_translate("window3", "Section:"))
        self.label_4.setText(_translate("window3", "Slot Type:"))
        item = self.subject_table.verticalHeaderItem(0)
        item.setText(_translate("window3", "Monday"))
        item = self.subject_table.verticalHeaderItem(1)
        item.setText(_translate("window3", "Tuesday"))
        item = self.subject_table.verticalHeaderItem(2)
        item.setText(_translate("window3", "Wednesday"))
        item = self.subject_table.verticalHeaderItem(3)
        item.setText(_translate("window3", "Thursday"))
        item = self.subject_table.verticalHeaderItem(4)
        item.setText(_translate("window3", "Friday"))
        item = self.subject_table.verticalHeaderItem(5)
        item.setText(_translate("window3", "Saturday"))
        item = self.subject_table.horizontalHeaderItem(0)
        item.setText(_translate("window3", "9:00-9:55"))
        item = self.subject_table.horizontalHeaderItem(1)
        item.setText(_translate("window3", "9:55-10:50"))
        item = self.subject_table.horizontalHeaderItem(2)
        item.setText(_translate("window3", "11:10-12:05"))
        item = self.subject_table.horizontalHeaderItem(3)
        item.setText(_translate("window3", "12:05-1:00"))
        item = self.subject_table.horizontalHeaderItem(4)
        item.setText(_translate("window3", "1:00-1:55"))
        item = self.subject_table.horizontalHeaderItem(5)
        item.setText(_translate("window3", "1:55-2:50"))
        item = self.subject_table.horizontalHeaderItem(6)
        item.setText(_translate("window3", "2:50-3:40"))
        item = self.subject_table.horizontalHeaderItem(7)
        item.setText(_translate("window3", "3:40-4:30"))
        self.label_2.setText(_translate("window3", "Semester:"))
        self.label.setText(_translate("window3", "Subject Constraints"))
        self.printBtn.setText(_translate("window3", "Print"))
        self.backBtn.setText(_translate("window3", "< Back"))
        self.nextBtn.setText(_translate("window3", "Next >"))
        self.menuFile.setTitle(_translate("window3", "File"))
        self.menuHelp.setTitle(_translate("window3", "Help"))
        self.actionSave.setText(_translate("window3", "Save"))
        self.actionLoad.setText(_translate("window3", "Load"))
        self.actionExit.setText(_translate("window3", "Exit"))
        self.actionAbout.setText(_translate("window3", "About"))
        self.actionManual.setText(_translate("window3", "Manual"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window3 = QtWidgets.QMainWindow()
    ui = Ui_window3()
    ui.setupUi(window3)
    window3.show()
    sys.exit(app.exec_())

