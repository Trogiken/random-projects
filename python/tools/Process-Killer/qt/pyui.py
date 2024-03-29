# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\test.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import processKiller as prskiller


class ProcessData:
    __instance = None

    @staticmethod
    def getInstance():
        return ProcessData.__instance
    
    # reset instance
    @staticmethod
    def resetInstance():
        ProcessData.__instance = None


    def __init__(self, process_list):
        self.processes = process_list

        ProcessData.__instance = self


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.killButton = QtWidgets.QPushButton(self.centralwidget)
        self.killButton.setGeometry(QtCore.QRect(500, 120, 81, 61))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)

        self.killButton.setFont(font)
        self.killButton.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.killButton.setObjectName("killButton")
        self.killButton.clicked.connect(self.killButtonClicked)

        self.searchField = QtWidgets.QLineEdit(self.centralwidget)
        self.searchField.setGeometry(QtCore.QRect(223, 120, 181, 51))
        self.searchField.setObjectName("searchField")


        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(420, 120, 75, 23))
        self.searchButton.setObjectName("searchButton")
        self.searchButton.clicked.connect(self.searchButtonClicked)

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(220, 190, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)  # allow multiple selections

        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(420, 150, 75, 23))
        self.resetButton.setObjectName("resetButton")
        self.resetButton.clicked.connect(self.resetButtonClicked)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionSearch = QtWidgets.QAction(MainWindow)
        self.actionSearch.setObjectName("actionSearch")
        self.actionSearch.triggered.connect(self.searchButtonClicked)
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionReset.triggered.connect(self.resetButtonClicked)

        self.menuOptions.addAction(self.actionSearch)
        self.menuOptions.addAction(self.actionReset)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Process Killer"))
        self.killButton.setToolTip(_translate("MainWindow", "Kill"))
        self.killButton.setStatusTip(_translate("MainWindow", "Kills the listed processes"))
        self.killButton.setText(_translate("MainWindow", "Kill"))
        self.searchField.setToolTip(_translate("MainWindow", "Input Search"))
        self.searchField.setStatusTip(_translate("MainWindow", "Process name or Close to"))
        self.searchButton.setToolTip(_translate("MainWindow", "Search"))
        self.searchButton.setStatusTip(_translate("MainWindow", "Search for processes matching input"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.resetButton.setToolTip(_translate("MainWindow", "Reset"))
        self.resetButton.setStatusTip(_translate("MainWindow", "Clears the input field"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionSearch.setText(_translate("MainWindow", "Search"))
        self.actionSearch.setShortcut(_translate("MainWindow", "Return"))
        self.actionReset.setText(_translate("MainWindow", "Reset"))
        self.actionReset.setShortcut(_translate("MainWindow", "Ctrl+Return"))


    def searchButtonClicked(self):
        self.listWidget.clear()
        ProcessData.resetInstance()

        user_query = self.searchField.text()
        data = ProcessData(process_list=prskiller.list_processes(user_query))
        if data.processes:  # check if any processes were found
            for prs in data.processes:
                self.listWidget.addItem(f'{prs["image_name"]}: {prs["pid"]}')
        else:
            pass
    
    def resetButtonClicked(self):
        ProcessData.resetInstance()
        self.searchField.clear()
        self.listWidget.clear()
    
    def killButtonClicked(self):
        data = ProcessData.getInstance()
        if data is None:
            return

        pid_kill_list = [process['pid'] for process in data.processes]  # extract pid's from processes
        stripped_list = [pid.strip('"') for pid in pid_kill_list]  # pass pid's with internal double quotes removed
        prskiller.kill_processes(stripped_list)

        ProcessData.resetInstance()
        self.searchField.clear()
        self.listWidget.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
