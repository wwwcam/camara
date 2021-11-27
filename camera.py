from PySide2.QtWidgets import QApplication, QMainWindow , QMessageBox ,QLabel ,QWidget, QSpinBox
from PySide2 import QtUiTools
from PySide2.QtCore import QTimer,QObject,Signal,QTime
from PySide2.QtGui import QColor
from PySide2 import QtGui ,QtWidgets ,QtCore
from PySide2.QtWidgets import * 
from PySide2 import QtCore, QtGui
from PySide2.QtGui import * 
from PySide2.QtCore import * 
import win32gui
import datetime
from datetime import timedelta
import subprocess
import win32con    
import pickle
import time
import psutil
import re
import win32gui,win32com.client,win32con
import traceback
from Socket_Singleton import Socket_Singleton
import threading
import sys
import btnEvent as bte

class MyMainWindow(QWidget):
    def __init__(self, parent=None):
        
        QWidget.__init__(self)
        print("?")
        self.dclickTime = [time.time() for i in range(37)]
        
        self.ui = QtUiTools.QUiLoader(parent=self).load("./camera_bt.ui" ,self  )
        self.ui.show()
        shadow = QGraphicsDropShadowEffect()
        # setting blur radius (optional step)
        shadow.setBlurRadius(10)
        shadow.setYOffset(50.5)
        # adding shadow to the label
        self.ui.splash_Scr.setStyleSheet("border : 10px solid black")
        self.ui.splash_Scr.setGraphicsEffect(shadow)
        
        btes = bte.btns(self)
        btes.dclickEvents()
        
        self.splashTimer = QTimer(self.ui)
        self.splashTimer.setInterval(3000)
        self.splashTimer.setSingleShot(True)
        self.splashTimer.timeout.connect(self.stopSplash)
        self.splashTimer.start()
        
        #self.setWindowState(self.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)
        #self.activateWindow()

        #self.show()
        #self.move(1920-765,1080-535-70)
        #self.setFixedSize(765,535)
        self.cameras = []
        for i in range(1,37):
                exec('self.cameras.append(self.ui.cmraBt_%02d)'%i)
        
    def stopSplash(self):
        self.ui.splash_Scr.hide()
            
            
    

if __name__ == '__main__':

    app = QApplication(sys.argv)
   
    ui = MyMainWindow()
    ui.show()
    sys.exit(app.exec_())
