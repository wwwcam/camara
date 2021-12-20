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
import imutils
import cv2
import psutil
import imutils
import re
import numpy as np
import win32gui,win32com.client,win32con
import traceback
from Socket_Singleton import Socket_Singleton
import threading
import sys,os
from btnEvent import  btns
from videoPlayer import vplayer
from settingPanel import Pannel
from saveSetting import saveSetting


try:
    os.mkdir("./save")
except:
    pass


def imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8): 
    try: 
        n = np.fromfile(filename, dtype) 
        img = cv2.imdecode(n, flags) 
        return img
    except: 
        import traceback
        return None

def imwrite(filename, img, params=None): 
    try: 
        ext = os.path.splitext(filename)[1] 
        result, n = cv2.imencode(ext, img, params) 
        if result: 
            with open(filename, mode='w+b') as f: 
                n.tofile(f) 
            return True 
        else: 
            return False 
    except: 
        import traceback
        return None

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
        self.mapPath = None
        self.btnClickTime = time.time()
        self.btnClickCnt = 0
        self.currentCam = None
        self.currenListtLayer = [i for i in range(32)]

        self.currentLayer =0 
        self.pannel = Pannel(self.settingLayer , "./camera_setting.ui" , self)


        vplayer.__init__(self )#vplayer 함수 로딩
        self.setFileName = "./datas/settings.pkl"
        
        btns.__init__(self , self.ui)  
        saveSetting.__init__(self)
        
        self.settings = {}
        self.currentLayer = 0
        self.loadSet()
        self.ui.cmr_listWidget_5.clear()

        self.ui.folferAddres.setText(self.settings['savepath'])
        

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

        self.onesectimer = QTimer(self.ui)
        self.onesectimer.setInterval(1000)
        self.onesectimer.timeout.connect(self.onesec)## 스플래시 스크린 숨기기 함수를 따로 만들지 않음
        self.onesectimer.start()


        #self.setlistcolors()
        self.showCameras = [self.cameras[cam] for cam in self.cameras]
        self.ui.folferSelect_Bt.clicked.connect(self.selectFolder)
        #print(dir(self.ui))
        self.ui.showRealtime.clicked.connect(self.Realtime)
        self.ui.showReplay.clicked.connect(self.Replay)
        self.ui.loadmap.clicked.connect(self.selectMap)
        self.ui.folferOpen_Bt.clicked.connect(self.openSaveFolder)
        self.ui.cmr_listWidget.currentItemChanged.connect(self.changelistColor)
        self.showBtnIcon( self.mapPath , self.ui.loadmap , (440,150))

        self.ui.widget_5.show()
        self.ui.replayWidget.hide()

        self.ui.closeEvent = self.closeEvent




        ### 비디오 플레이를 위한 타이머 추가
        #self.vp1 = QTimer(self.ui)
        #self.vp1.setInterval(10)
        #self.vp1.timeout.connect(self.playV1)
        #self.vp1.start()

    def openSaveFolder(self):
        os.startfile(os.path.abspath(self.savePath))


    def Realtime(self):
        self.ui.widget_5.show()
        self.ui.replayWidget.hide()
    def Replay(self):
        self.ui.widget_5.hide()
        self.ui.replayWidget.show()

    def onesec(self):
        dt = datetime.datetime.now().isoformat()[:19].replace("T" , " ")
        self.ui.timeedit.setText(dt)
    def setlistcolors(self):
        for i in range(11):
            self.ui.cmr_listWidget.item(i).setBackgroundColor(QColor(0,0,0,100))
        for i in range(11):
            self.ui.cmr_listWidget_3.item(i).setBackgroundColor(QColor(0,0,0,100))
        for i in range(10):
            self.ui.cmr_listWidget_4.item(i).setBackgroundColor(QColor(0,0,0,100))
                    
    def changelistColor(self):
        colors = []
        self.currenListtLayer = []
        self.cntLayers = [32 , 6,7,7,10,13]
        for i in range(11):
            green = self.ui.cmr_listWidget.item(i).backgroundColor().toRgb().green()
            if green == 255:
                colors.append(1)
                self.currenListtLayer.append(i)
        for i in range(11):
            green = self.ui.cmr_listWidget_3.item(i).backgroundColor().toRgb().green()
            if green == 255:
                colors.append(1)
                self.currenListtLayer.append(i+11)
        for i in range(10):
            green = self.ui.cmr_listWidget_4.item(i).backgroundColor().toRgb().green()
            if green == 255:
                colors.append(1)
                self.currenListtLayer.append(i+22)

        if self.currentLayer > 0:
            if sum(colors) < self.cntLayers[self.currentLayer]:
                green = self.ui.cmr_listWidget.currentItem().backgroundColor().toRgb().green()
                if green == 255:
                    self.ui.cmr_listWidget.currentItem().setBackgroundColor(QColor(0,0,0,100))
                else:
                    self.ui.cmr_listWidget.currentItem().setBackgroundColor(QColor(0,255,0,100))


    def selectFolder(self):
        self.savePath = self.settings['savepath'] = self.savePath = QtWidgets.QFileDialog.getExistingDirectory(self.ui, '저장 폴더를 선택해 주세요' , self.savePath)
        self.ui.folferAddres.setText(self.settings['savepath'])
        self.saveSet()

    def showBtnIcon(self , img , icon , size):
        icon.setIconSize(QtCore.QSize(size[0],size[1]))
        image = imread(img)
        image = cv2.resize(image,[440,150], interpolation=cv2.INTER_AREA)
        bytesPerLine = 3 * image.shape[1]
        image = QtGui.QImage(image.data, image.shape[1], image.shape[0], bytesPerLine  , QtGui.QImage.Format_RGB888).rgbSwapped()
        icon.setIcon(QPixmap.fromImage(image)) 

    def selectMap(self):
        if time.time() - self.btnClickTime < 0.3:
            self.btnClickCnt+=1
            if self.btnClickCnt > 5:
                if self.mapPath:
                    mapdir = os.path.dirname(self.mapPath)
                else:
                    mapdir = "c:/"
                self.mapPath = self.settings['mapPath']  = QtWidgets.QFileDialog.getOpenFileName(self.ui, '지도파일을 선택해주세요. 크기는 440X150입니다' , mapdir , "JPEG (*.jpg *.jpeg);;PNG (*.png)")[0]
                
                self.showBtnIcon( self.mapPath , self.ui.loadmap , (440,150))
                  
                self.saveSet()
        else:
            self.btnClickCnt = 0
        self.btnClickTime = time.time()



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
