from PySide2.QtWidgets import QApplication, QMainWindow , QMessageBox ,QLabel ,QWidget, QSpinBox
from PySide2 import QtUiTools
from PySide2.QtCore import QTimer,QObject,Signal,QTime
from PySide2.QtGui import QColor
from PySide2 import QtGui ,QtWidgets ,QtCore
from PySide2.QtWidgets import * 
from PySide2.QtGui import * 
from PySide2.QtCore import * 
import datetime
from datetime import timedelta
import subprocess
import pickle
import time
import cv2
import psutil
import re
import win32gui,win32com.client,win32con
import traceback
from Socket_Singleton import Socket_Singleton
import threading
import sys
from btnEvent import  btns
from videoPlayer import vplayer
from settingPanel import Pannel
class MyMainWindow(QWidget,btns , vplayer): #클래스로 직접 적용하였음.
    def __init__(self, parent=None):
        
        QWidget.__init__(self)
        vplayer.__init__(self)#vplayer 함수 로딩
        self.ui = QtUiTools.QUiLoader(parent=self).load("./camera_bt.ui" ,self  )
        btns.__init__(self , self.ui)   
        self.pannel = Pannel(self.ui , "./camera_setting.ui")
        self.ui.widget_9 = self.pannel.ui.widget_9
        self.ui.widget_9.move(1500,100)#왜 안보이지????

        ################## 스플래시 스크린에 입체 그림자 적용, 잘 안됨##################
        #self.pannel.ui.widget_9.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        #self.pannel.ui.widget_9.hide()
        #shadow = QGraphicsDropShadowEffect()
        # setting blur radius (optional step)
        #shadow.setBlurRadius(10)
        #shadow.setYOffset(50.5)d
        # adding shadow to the label
        #self.ui.splash_Scr.setStyleSheet("border : 10px solid black")
        #self.ui.splash_Scr.setGraphicsEffect(shadow)
        ###################################################################################

        self.splashTimer = QTimer(self.ui)
        self.splashTimer.setInterval(3000)
        self.splashTimer.setSingleShot(True)
        self.splashTimer.timeout.connect(self.ui.splash_Scr.hide)## 스플래시 스크린 숨기기 함수를 따로 만들지 않음
        self.splashTimer.start()
        

        ### 비디오 플레이를 위한 타이머 추가
        self.vp1 = QTimer(self.ui)
        self.vp1.setInterval(33)
        self.vp1.timeout.connect(self.playV1)
        self.vp1.start()



            
            
    

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ui = MyMainWindow()
    ui.ui.show()
    sys.exit(app.exec_())
