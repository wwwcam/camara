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
import imutils
import re
import win32gui,win32com.client,win32con
import traceback
from Socket_Singleton import Socket_Singleton
import threading
import sys
from btnEvent import  btns
from videoPlayer import vplayer
from settingPanel import Pannel
from saveSetting import saveSetting
class MyMainWindow(QWidget,btns , vplayer,saveSetting): #클래스로 직접 적용하였음.
    def __init__(self, parent=None):
        QWidget.__init__(self)
        multiprocessing.freeze_support()
        self.ui = QtUiTools.QUiLoader(parent=self).load("./camera_bt.ui" ,self  )
        self.settingLayer = QWidget(self.ui)
        self.settingLayer.resize(259 , 850)
        self.settingLayer.setStyleSheet(u"background-color: rgba(50, 50, 80, 50);")
        self.settingLayer.move(1650 , 10)
        self.settingLayer.hide()
        self.stopVideos = 0
        
        
        self.pannel = Pannel(self.settingLayer , "./camera_setting.ui")


        vplayer.__init__(self )#vplayer 함수 로딩
        self.setFileName = "./datas/settings.pkl"
        btns.__init__(self , self.ui)  
        saveSetting.__init__(self)
        
        self.settings = {}
        self.layers = []
        self.currentLayer = 0
        self.loadSet()


        

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
        
        self.videoTimer = QTimer(self.ui)
        self.videoTimer.setInterval(30)
        self.videoTimer.timeout.connect(self.videoLoop)## 스플래시 스크린 숨기기 함수를 따로 만들지 않음
        self.videoTimer.start()

        self.fiveSecTimer = QTimer(self.ui)
        self.fiveSecTimer.setInterval(2000)
        self.fiveSecTimer.timeout.connect(self.tout2)## 스플래시 스크린 숨기기 함수를 따로 만들지 않음
        self.fiveSecTimer.start()

        self.ui.folferSelect_Bt.clicked.connect(self.selectFolder)

        self.ui.closeEvent = self.closeEvent



        ### 비디오 플레이를 위한 타이머 추가
        #self.vp1 = QTimer(self.ui)
        #self.vp1.setInterval(10)
        #self.vp1.timeout.connect(self.playV1)
        #self.vp1.start()


    def selectFolder(self):
        self.settings['savepath'] = self.savePath = QtWidgets.QFileDialog.getExistingDirectory(self.ui, '저장 폴더를 선택해 주세요' , self.savePath)



    def tout2(self):
        pass


    def videoLoop(self):
        for cam in self.Qs:
            q = self.Qs[cam]
            cvimg =None
            btn = self.cameras[cam]
            #if q[0].qsize() > 1:
                #print("q[0].qsize()" , q[0].qsize())
            for idx in range(q[0].qsize()):
                cvimg = q[0].get()
            if type(cvimg) != type(None):
                if cvimg.shape == (1,1,3):
                    self.setLayerCorlr()
                    self.setCamText()
                    self.stopVideos = time.time()
                else:
                    cvimg = imutils.resize(cvimg , height = btn.iconSize().height())
                bytesPerLine = 3 * cvimg.shape[1]
                image = QtGui.QImage(cvimg.data, cvimg.shape[1], cvimg.shape[0], bytesPerLine  , QtGui.QImage.Format_RGB888).rgbSwapped()
                btn.setIcon(QPixmap.fromImage(image))   
                btn.setText('')
                if btn.iconSize() != btn.size():
                    btn.setIconSize(btn.size())
            

    def setupUi(self):
        pass

    def closeEvent(self,e):
        print("ok")
            
            
    

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()
    app = QApplication(sys.argv)
    ui = MyMainWindow()
    ui.setupUi()
    ui.ui.show()
    sys.exit(app.exec_())
