# importing libraries
from PySide2.QtWidgets import * 
from PySide2 import QtCore, QtGui
from PySide2.QtGui import * 
from PySide2.QtCore import * 
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(308, 387)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 308, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
 
        for children in self.centralwidget.findChildren(QWidget):
            shadow = QGraphicsDropShadowEffect(blurRadius=5, xOffset=3, yOffset=3)
            children.setGraphicsEffect(shadow)
 
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.pushButton.setText(QApplication.translate("MainWindow", "PushButton", None, -1))
 
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())