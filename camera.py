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
import pyautogui as pag
import cv2
import psutil
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
        self.ui = QtUiTools.QUiLoader(parent=self).load("./cmr_bt1.ui" ,self  )
        self.settingLayer = QWidget(self.ui)
        self.settingLayer.resize(259 , 831)
        self.settingLayer.setStyleSheet(u"background-color: rgba(50, 50, 80, 50);")
        self.settingLayer.move(1567 , 80)
        self.settingLayer.hide()
        self.stopVideos = 0
        self.baseCamNum = 0
        self.allStoped = True
        
        self.mapPath = None
        self.inBaseSet = False
        self.btnClickTime = time.time()
        self.btnClickCnt = 0
        self.currentCam = None
        self.currenListtLayer = [i for i in range(32)]
        self.currentLayer = 0 
        self.pannel = Pannel(self.settingLayer , "./camera_setting.ui" , self)
        vplayer.__init__(self )#vplayer 함수 로딩
        self.setFileName = "./datas/settings.pkl"
        btns.__init__(self , self.ui)  
        saveSetting.__init__(self)
        self.settings = {}
        self.currentLayer = 0

        self.camBaseSettings = {}
        for i in range(50):
            self.camBaseSettings[i] = {"ip":'' , "name":f'cam{i:02d}' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''}
        self.settings['camsetting'] = self.camBaseSettings
        self.loadSet()
        
        self.ui.cmr_listWidget_5.clear()
        if 'savepath' in self.settings:
            if os.path.isdir(self.settings['savepath']):
                self.ui.folferAddres.setText(self.settings['savepath'])
            else:
                self.ui.folferAddres.setText(os.path.abspath("./"))
                self.settings['savepath'] = os.path.abspath("./")

        else:
            self.ui.folferAddres.setText(os.path.abspath("./"))
            self.settings['savepath'] = os.path.abspath("./")

        self.inFullScreenMode = False

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

        self.ui.gsetLayer.hide()
        self.ui.showReplay_2.clicked.connect(self.ui.gsetLayer.show)
        self.ui.gsetClose.clicked.connect(self.ui.gsetLayer.hide)


        #self.setlistcolors()
        self.showCameras = [self.cameras[cam] for cam in self.cameras]
        self.ui.folferSelect_Bt.clicked.connect(self.selectFolder)
        #print(dir(self.ui))
        self.ui.showRealtime.clicked.connect(self.Realtime)
        self.ui.showReplay.clicked.connect(self.Replay)
        self.ui.accountManager.clicked.connect(self.showManager)
        self.ui.accountManager_2.clicked.connect(self.showManager2)
        self.ui.loadmap.clicked.connect(self.selectMap)
        self.ui.folferOpen_Bt.clicked.connect(self.openSaveFolder)
        self.ui.addUser.clicked.connect(self.newmember)
        self.ui.changePwd.clicked.connect(self.pwdChanged)
        self.ui.logIn.clicked.connect(self.userlogin)
        
        #self.ui.cmr_listWidget.currentItemChanged.connect(self.changelistColor)
        self.showBtnIcon( self.mapPath , self.ui.loadmap , (440,150))
        self.ui.widget_3.show()
        self.ui.replayWidget.hide()

        self.ui.newPwdlb.hide()
        self.ui.newPwd.hide()
        self.ui.newPwd2.hide()
        self.ui.newPwdlb2.hide()
        self.ui.changePwd.hide()
        self.ui.addUser.hide()
        self.ui.accountManager.move(30 , 150)
        self.ui.accountManager_2.move(205 , 150)
        self.ui.accountManager.setDisabled(True)
        self.ui.accountManager_2.setDisabled(True)

        self.ui.allStart.setDisabled(True)
        self.ui.allStop.setDisabled(True)


    def pwdChanged(self):
        uid = self.ui.userId.text().strip()
        upass3 = self.ui.userPwd.text().strip() 
        upass1 = self.ui.newPwd.text().strip() 
        upass2 = self.ui.newPwd2.text().strip() 

        if uid not in self.settings['userInfo']:
            QMessageBox.information(self.ui , "정보" , "아이디를 확인하세요")
            return

        if self.settings['userInfo'][uid] != upass3:
            QMessageBox.information(self.ui , "정보" , "기존 비번을 확인하세요")
            return
        
        if len(uid) < 5:
            QMessageBox.information(self.ui , "정보" , "새 비밀번호를 5자 이상 입력하세요")
            return
            
        if upass1 != upass2:
            QMessageBox.information(self.ui , "정보" , "새 비밀번호가 일치 하지 않습니다.")
            return

        self.settings['userInfo'][uid] = upass1
        with open(self.setFileName, "wb") as f:
            pickle.dump(self.settings , f)

        QMessageBox.information(self.ui , "정보" , "변경 되었습니다.")


    def newmember(self):
        uid = self.ui.userId.text().strip()
        
        upass1 = self.ui.newPwd.text().strip() 
        upass2 = self.ui.newPwd2.text().strip() 


        if len(uid) < 5:
            QMessageBox.information(self.ui , "정보" , "아이디를 5자 이상 입력하세요")
            return
        
        if len(uid) < 5:
            QMessageBox.information(self.ui , "정보" , "비밀번호를 5자 이상 입력하세요")
            return

        if upass1 != upass2:
            QMessageBox.information(self.ui , "정보" , "비밀번호가 일치 하지 않습니다.")
            return
        
        self.settings['userInfo'][uid] = upass1
        with open(self.setFileName, "wb") as f:
            pickle.dump(self.settings , f)
        QMessageBox.information(self.ui , "정보" , "맴버가 생성 되었습니다.")



    def userlogin(self):
        uid = self.ui.userId.text().strip()
        upass = self.ui.userPwd.text().strip()
        if uid not in self.settings['userInfo']:
            QMessageBox.information(self.ui , "정보" , "아이디를 확인하세요")
            return
        if self.settings['userInfo'][uid] != upass:
            QMessageBox.information(self.ui , "정보" , "비번을 확인하세요")
            return
        QMessageBox.information(self.ui , "정보" , "로그인 되었습니다")
        self.ui.accountManager.setDisabled(False)
        self.ui.allStart.setDisabled(False)
        self.ui.allStop.setDisabled(False)


        

    def showManager2(self):
        self.ui.userId.clear()
        self.ui.userPwd.clear()
        if self.ui.newPwdlb.isHidden():
            self.ui.newPwdlb.show()
            self.ui.newPwd.show()
            self.ui.newPwd2.show()
            self.ui.newPwdlb2.show()
            self.ui.changePwd.show()
            self.ui.addUser.hide()
            self.ui.changePwd.show()
            self.ui.logIn.hide()
            self.ui.accountManager.hide()
            self.ui.accountManager.move(30 , 225)
            self.ui.accountManager_2.move(205 , 225)
        else:
            self.ui.newPwdlb.hide()
            self.ui.newPwd.hide()
            self.ui.newPwd2.hide()
            self.ui.newPwdlb2.hide()
            self.ui.changePwd.hide()
            self.ui.logIn.show()    
            self.ui.accountManager.show()
            self.ui.accountManager.move(30 , 150)
            self.ui.accountManager_2.move(205 , 150)


    def showManager(self):
        self.ui.userId.clear()
        self.ui.userPwd.clear()
        if self.ui.newPwdlb.isHidden():
            self.ui.newPwdlb.show()
            self.ui.newPwd.show()
            self.ui.newPwd2.show()
            self.ui.newPwdlb2.show()
            self.ui.changePwd.show()
            self.ui.addUser.show()
            self.ui.label_12.hide()
            self.ui.userPwd.hide()
            self.ui.changePwd.hide()
            self.ui.logIn.hide()
            self.ui.accountManager_2.hide()
            self.ui.accountManager.move(30 , 225)
            self.ui.accountManager_2.move(205 , 225)
        else:
            self.ui.newPwdlb.hide()
            self.ui.newPwd.hide()
            self.ui.newPwd2.hide()
            self.ui.newPwdlb2.hide()
            self.ui.changePwd.hide()
            self.ui.addUser.hide()
            self.ui.label_12.show()
            self.ui.userPwd.show()
            self.ui.changePwd.show()
            self.ui.logIn.show()
            self.ui.accountManager_2.show()
            self.ui.accountManager.move(30 , 150)
            self.ui.accountManager_2.move(205 , 150)

    def openSaveFolder(self):
        os.startfile(os.path.abspath(self.savePath))

    def Realtime(self):
        self.allStop(noask=True)
        self.ui.widget_3.show()
        self.ui.replayWidget.hide()

    def Replay(self):
        self.allStop(noask=True)
        self.ui.widget_3.hide()
        self.ui.replayWidget.show()

    def onesec(self):
        dt = datetime.datetime.now().isoformat()[:19].replace("T" , " ")
        self.ui.timeedit.setText(dt)
        check = False
        for cam in self.cameras:
            size = self.cameras[cam].size()
            w = size.width()
            if w == 1411:
                check = True
                break
        #print("check" , check)
        if check == False:
            self.inFullScreenMode = False
            

    def setlistcolors(self):
        return
        for i in range(11):
            self.ui.cmr_listWidget.item(i).setBackgroundColor(QColor(0,0,0,100))
        for i in range(11):
            self.ui.cmr_listWidget_3.item(i).setBackgroundColor(QColor(0,0,0,100))
        for i in range(10):
            self.ui.cmr_listWidget_4.item(i).setBackgroundColor(QColor(0,0,0,100))



    def changelistColor(self):
        return
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
        if img:
            icon.setIconSize(QtCore.QSize(size[0],size[1]))
            if os.path.isfile(img):
                image = imread(img)
                image = cv2.resize(image,dsize=(371,141), interpolation=cv2.INTER_AREA)
                bytesPerLine = 3 * image.shape[1]
                image = QtGui.QImage(image.data, image.shape[1], image.shape[0], bytesPerLine  , QtGui.QImage.Format_RGB888).rgbSwapped()
                icon.setIcon(QPixmap.fromImage(image)) 

    def selectMap(self):
        print("ok",time.time() - self.btnClickTime)
        if time.time() - self.btnClickTime < 0.3:
            self.btnClickCnt+=1
            if self.btnClickCnt > 5:
                if self.mapPath:
                    mapdir = os.path.dirname(self.mapPath)
                else:
                    mapdir = "c:/"
                self.mapPath = self.settings['mapPath']  = QtWidgets.QFileDialog.getOpenFileName(self.ui, '지도파일을 선택해주세요' , mapdir , "JPEG (*.jpg *.jpeg);;PNG (*.png)")[0]
                if self.mapPath and os.path.isfile(self.mapPath):
                    self.showBtnIcon( self.mapPath , self.ui.loadmap , (440,150))                  
                self.saveSet()
        else:
            self.btnClickCnt = 0
        self.btnClickTime = time.time()

    def tout2(self):
        pass

    def videoLoop(self):
        self.mpos = pag.position()
        geo = self.ui.geometry()
        x = geo.x()
        y = geo.y()
        if self.ui.isActiveWindow():
            if (self.settingLayer.isHidden() == False) and self.inFullScreenMode and self.inBaseSet:
                self.inBaseSet = False
                print("self.inBaseSet = False??" , self.inBaseSet)
                self.settingLayer.hide()   
            if x+1600 < self.mpos[0]:
                if self.settingLayer.isHidden() and self.inFullScreenMode:
                    self.settingLayer.resize(259 , 831)
                    self.settingLayer.move(1567 , 80)
                    self.settingLayer.setStyleSheet(u"background-color: rgba(50, 50, 80, 50);")
                    self.settingLayer.show()     

            else:
                if self.inBaseSet ==False:
                    self.settingLayer.hide()
        for cam in self.Qs:
            q = self.Qs[cam]
            cvimg =None
            btn = self.cameras[cam]
            #if q[0].qsize() > 1:
                #print("q[0].qsize()" , q[0].qsize())
            for idx in range(q[0].qsize()):
                qv = q[0].get()
                if len(qv) == 3:
                    cvimg , alarm , name = qv
                else:
                    print(qv)
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
                btn.alarm.setText("   " + name)   
                if alarm:
                    btn.alarm.setStyleSheet("background-color: rgba(255, 50, 100, 100);") 
                   
                else:
                    btn.alarm.setStyleSheet("background-color: rgba(255, 255, 255, 100);")  

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
