import cv2 
import imutils
import numpy as np
import time
from PySide2.QtWidgets import QApplication, QMainWindow , QMessageBox ,QLabel ,QWidget, QSpinBox
from PySide2 import QtUiTools
from PySide2.QtCore import QTimer,QObject,Signal,QTime
from PySide2.QtGui import QColor
from PySide2 import QtGui ,QtWidgets ,QtCore
from PySide2.QtWidgets import * 
from PySide2.QtGui import * 
from PySide2.QtCore import * 
import pickle
import os



class saveSetting():
    def __init__(self):
        self.setpanel = self.pannel.ui
        self.emptyCam = 'font: 75 14pt "맑은 고딕";color: rgb(255, 255, 255);background-color: rgba(61, 63, 67,200);'
        self.setpanel.saveButton.clicked.connect(self.saveSet)
        self.camlayers = [
            ["cam%02d"%i for i in range(1,33)],
            [],
            [],
            []
        ]
        self.setLayerCorlr()
        self.setCamText()



    def setLayerCorlr(self):
        for cam in self.camlayers[self.currentLayer]:
            if self.camSettings[self.currentLayer][cam]["ip"]:
                self.cameras[cam].setStyleSheet('font: 75 14pt "맑은 고딕";color: rgb(255, 255, 255);background-color: rgba(5, 40, 60 , 100);')
            else:
                self.cameras[cam].setStyleSheet(self.emptyCam)

    def setCamText(self):
        for cam in self.camlayers[self.currentLayer]:
            name =self.camSettings[self.currentLayer][cam]["name"].strip()
            if name :
                self.cameras[cam].setText(name)
            else:
                self.cameras[cam].setText(cam)


    def loadSet(self ):
        if os.path.isfile(self.setFileName):
            with open(self.setFileName, "rb") as f:
                self.settings = pickle.load(f)
                self.camSettings = self.settings['camsetting']
                if 'camBaseSet' in self.settings:
                    self.camBaseSettings = self.settings['camBaseSet']
                else:
                    self.camBaseSettings = {}
                    for i in range(32):
                        self.camBaseSettings[i] = {"ip":'' , "name":f'cam{i+1:02d}' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''}
                
                if "userInfo" in self.settings:
                    self.userInfo = self.settings['userInfo']
                else:
                    self.userInfo = self.settings['userInfo'] = {}

                if 'mapPath' in  self.settings:
                    self.mapPath = self.settings['mapPath']
                else:
                    self.mapPath = None

                if 'currentLayer' in self.settings:
                    self.currentLayer = self.settings['currentLayer']
                else:
                    self.currentLayer = 0
                if 'savepath' in self.settings:
                    self.savePath = self.settings['savepath']
                else:
                    self.savePath = "./save"
                    self.settings['savepath'] = self.savePath

            self.setLayerCorlr()

        return self.settings

                

    def loadCameraSet(self , base = False):
        if self.inBaseSet:
            self.setpanel.ip_lineEdit_7.setText(self.camBaseSettings[self.baseCamNum]["ip"])
            self.setpanel.camera_lineEdit_7.setText(self.camBaseSettings[self.baseCamNum]["name"])
            self.setpanel.loca_lineEdit_7.setText(self.camBaseSettings[self.baseCamNum]["location"])
            self.setpanel.zoom_horizontalSlider_7.setValue(self.camBaseSettings[self.baseCamNum]["zoom"])
            self.setpanel.sens_horizontalSlider_7.setValue(self.camBaseSettings[self.baseCamNum]["sens"])
            self.setpanel.foco_horizontalSlider_7.setValue(self.camBaseSettings[self.baseCamNum]["focus"])
            self.setpanel.memo_textEdit_7.setPlainText(self.camBaseSettings[self.baseCamNum]["memo"])
        else:
            if self.currentCam:
                self.setpanel.ip_lineEdit_7.setText(self.camSettings[self.currentLayer][self.currentCam]["ip"])
                self.setpanel.camera_lineEdit_7.setText(self.camSettings[self.currentLayer][self.currentCam]["name"])
                self.setpanel.loca_lineEdit_7.setText(self.camSettings[self.currentLayer][self.currentCam]["location"])
                self.setpanel.zoom_horizontalSlider_7.setValue(self.camSettings[self.currentLayer][self.currentCam]["zoom"])
                self.setpanel.sens_horizontalSlider_7.setValue(self.camSettings[self.currentLayer][self.currentCam]["sens"])
                self.setpanel.foco_horizontalSlider_7.setValue(self.camSettings[self.currentLayer][self.currentCam]["focus"])
                self.setpanel.memo_textEdit_7.setPlainText(self.camSettings[self.currentLayer][self.currentCam]["memo"])


    def saveSet(self , base=False ):
        if self.inBaseSet:
            self.camBaseSettings[self.baseCamNum]["ip"] = self.setpanel.ip_lineEdit_7.text().strip()
            self.camBaseSettings[self.baseCamNum]["name"] = self.setpanel.camera_lineEdit_7.text().strip()
            self.camBaseSettings[self.baseCamNum]["location"] = self.setpanel.loca_lineEdit_7.text().strip()
            self.camBaseSettings[self.baseCamNum]["zoom"] = self.setpanel.zoom_horizontalSlider_7.value()
            self.camBaseSettings[self.baseCamNum]["sens"] = self.setpanel.sens_horizontalSlider_7.value()
            self.camBaseSettings[self.baseCamNum]["focus"] = self.setpanel.foco_horizontalSlider_7.value()
            self.camBaseSettings[self.baseCamNum]["memo"] = self.setpanel.memo_textEdit_7.toPlainText().strip()
            self.settings['camBaseSet'] = self.camBaseSettings
        else:
            if self.currentCam:
                self.camSettings[self.currentLayer][self.currentCam]["ip"] = self.setpanel.ip_lineEdit_7.text().strip()
                self.camSettings[self.currentLayer][self.currentCam]["name"] = self.setpanel.camera_lineEdit_7.text().strip()
                self.camSettings[self.currentLayer][self.currentCam]["location"] = self.setpanel.loca_lineEdit_7.text().strip()
                self.camSettings[self.currentLayer][self.currentCam]["zoom"] = self.setpanel.zoom_horizontalSlider_7.value()
                self.camSettings[self.currentLayer][self.currentCam]["sens"] = self.setpanel.sens_horizontalSlider_7.value()
                self.camSettings[self.currentLayer][self.currentCam]["focus"] = self.setpanel.foco_horizontalSlider_7.value()
                self.camSettings[self.currentLayer][self.currentCam]["memo"] = self.setpanel.memo_textEdit_7.toPlainText().strip()
                self.settings['camsetting'] = self.camSettings
                self.settings['currentLayer'] = self.currentLayer
                self.settings['selectedCams'] = self.currenListtLayer
        self.settings['savepath'] = self.savePath
        self.settings['mapPath'] = self.mapPath
        with open(self.setFileName, "wb") as f:
            pickle.dump(self.settings , f)

