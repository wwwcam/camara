import time
import copy
from PySide2.QtWidgets import QApplication, QMainWindow , QMessageBox ,QLabel ,QWidget, QSpinBox
from PySide2 import QtUiTools
from PySide2.QtCore import QTimer,QObject,Signal,QTime
from PySide2.QtGui import QColor
from PySide2 import QtGui ,QtWidgets ,QtCore
from PySide2.QtWidgets import * 
from PySide2.QtGui import * 
from PySide2.QtCore import * 
from multiprocessing import Process , Queue
import multiprocessing
class btns():
    def __init__(self , ui):
        self.ui = ui
        tmp = {
        "cam01":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam02":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam03":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam04":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam05":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam06":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam07":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam08":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam09":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam10":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam11":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam12":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam13":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam14":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam15":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam16":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam17":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam18":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam19":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam20":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam21":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam22":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam23":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam24":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam25":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam26":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam27":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam28":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam29":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam30":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam31":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},
        "cam32":{"ip":'' , "name":'' , "zoom":0 , "sens":0 , "focus":0 , "memo" : "" , "location":''},}
        self.camSettings = [copy.deepcopy(tmp) for i in range(30)]
        self.dclickTime = [time.time() for i in range(37)]

        self.ui.functionBt_01.clicked.connect(self.showall)
        self.ui.functionBt_02.clicked.connect(self.showLayer1)
        self.ui.functionBt_03.clicked.connect(self.showLayer2)
        self.ui.functionBt_04.clicked.connect(self.showLayer3)
        self.ui.functionBt_05.clicked.connect(self.showLayer4)
        self.ui.functionBt_06.clicked.connect(self.showLayer5)

        self.ui.cmraBt_01.clicked.connect(self.fullscreen01)
        self.ui.cmraBt_02.clicked.connect(self.fullscreen02)
        self.ui.cmraBt_03.clicked.connect(self.fullscreen03)
        self.ui.cmraBt_04.clicked.connect(self.fullscreen04)
        self.ui.cmraBt_05.clicked.connect(self.fullscreen05)
        self.ui.cmraBt_06.clicked.connect(self.fullscreen06)
        self.ui.cmraBt_07.clicked.connect(self.fullscreen07)
        self.ui.cmraBt_08.clicked.connect(self.fullscreen08)
        self.ui.cmraBt_09.clicked.connect(self.fullscreen09)
        self.ui.cmraBt_10.clicked.connect(self.fullscreen10)
        self.ui.cmraBt_11.clicked.connect(self.fullscreen11)
        self.ui.cmraBt_12.clicked.connect(self.fullscreen12)
        self.ui.cmraBt_13.clicked.connect(self.fullscreen13)
        self.ui.cmraBt_14.clicked.connect(self.fullscreen14)
        self.ui.cmraBt_15.clicked.connect(self.fullscreen15)
        self.ui.cmraBt_16.clicked.connect(self.fullscreen16)
        self.ui.cmraBt_17.clicked.connect(self.fullscreen17)
        self.ui.cmraBt_18.clicked.connect(self.fullscreen18)
        self.ui.cmraBt_19.clicked.connect(self.fullscreen19)
        self.ui.cmraBt_20.clicked.connect(self.fullscreen20)
        self.ui.cmraBt_21.clicked.connect(self.fullscreen21)
        self.ui.cmraBt_22.clicked.connect(self.fullscreen22)
        self.ui.cmraBt_23.clicked.connect(self.fullscreen23)
        self.ui.cmraBt_24.clicked.connect(self.fullscreen24)
        self.ui.cmraBt_25.clicked.connect(self.fullscreen25)
        self.ui.cmraBt_26.clicked.connect(self.fullscreen26)
        self.ui.cmraBt_27.clicked.connect(self.fullscreen27)
        self.ui.cmraBt_28.clicked.connect(self.fullscreen28)
        self.ui.cmraBt_29.clicked.connect(self.fullscreen29)
        self.ui.cmraBt_30.clicked.connect(self.fullscreen30)
        self.ui.cmraBt_31.clicked.connect(self.fullscreen31)
        self.ui.cmraBt_32.clicked.connect(self.fullscreen32)
        self.cameras = {"cam01" : self.ui.cmraBt_01, "cam02" : self.ui.cmraBt_02, "cam03" : self.ui.cmraBt_03, 
                        "cam04" : self.ui.cmraBt_04, "cam05" : self.ui.cmraBt_05, "cam06" : self.ui.cmraBt_06, "cam07" : self.ui.cmraBt_07, 
                        "cam08" : self.ui.cmraBt_08, "cam09" : self.ui.cmraBt_09, "cam10" : self.ui.cmraBt_10, "cam11" : self.ui.cmraBt_11, 
                        "cam12" : self.ui.cmraBt_12, "cam13" : self.ui.cmraBt_13, "cam14" : self.ui.cmraBt_14, "cam15" : self.ui.cmraBt_15, 
                        "cam16" : self.ui.cmraBt_16, "cam17" : self.ui.cmraBt_17, "cam18" : self.ui.cmraBt_18, "cam19" : self.ui.cmraBt_19, 
                        "cam20" : self.ui.cmraBt_20, "cam21" : self.ui.cmraBt_21, "cam22" : self.ui.cmraBt_22, "cam23" : self.ui.cmraBt_23, 
                        "cam24" : self.ui.cmraBt_24, "cam25" : self.ui.cmraBt_25, "cam26" : self.ui.cmraBt_26, "cam27" : self.ui.cmraBt_27, 
                        "cam28" : self.ui.cmraBt_28, "cam29" : self.ui.cmraBt_29, "cam30" : self.ui.cmraBt_30, "cam31" : self.ui.cmraBt_31, 
                        "cam32" : self.ui.cmraBt_32}

        for cam in self.cameras:
            self.cameras[cam].full = False
            self.cameras[cam].active = True

        self.fullscreens = [self.showall ,self.showLayer1 ,self.showLayer2 ]
        self.layers = {
            "6":[self.ui.cmraBt_01,
            self.ui.cmraBt_03,
            self.ui.cmraBt_09,
            self.ui.cmraBt_13,
            self.ui.cmraBt_14,
            self.ui.cmraBt_15
            ],
            "7_1":
            [self.ui.cmraBt_01,
            self.ui.cmraBt_04,
            self.ui.cmraBt_10,
            self.ui.cmraBt_16,
            self.ui.cmraBt_19,
            self.ui.cmraBt_20,
            self.ui.cmraBt_21,
            self.ui.cmraBt_22
            ],
            "7_2":
            [self.ui.cmraBt_01,
            self.ui.cmraBt_03,
            self.ui.cmraBt_13,
            self.ui.cmraBt_14,
            self.ui.cmraBt_15,
            self.ui.cmraBt_19,
            self.ui.cmraBt_20
            ],
            "10":
            [self.ui.cmraBt_01,
            self.ui.cmraBt_03,
            self.ui.cmraBt_13,
            self.ui.cmraBt_14,
            self.ui.cmraBt_15,
            self.ui.cmraBt_16,
            self.ui.cmraBt_19,
            self.ui.cmraBt_20,
            self.ui.cmraBt_21,
            self.ui.cmraBt_22,
            ],
            "13":
            [self.ui.cmraBt_01,
            self.ui.cmraBt_03,
            self.ui.cmraBt_04,
            self.ui.cmraBt_07,
            self.ui.cmraBt_08,
            self.ui.cmraBt_13,
            self.ui.cmraBt_14,
            self.ui.cmraBt_15,
            self.ui.cmraBt_16,
            self.ui.cmraBt_19,
            self.ui.cmraBt_20,
            self.ui.cmraBt_21,
            self.ui.cmraBt_22,
            ],

        }
 
    def showall(self):
        self.currentLayer = 0
        self.setlistcolors()
        self.changelistColor()
        for cidx  , cam in enumerate(self.cameras):
            self.cameras[cam].active=True
            self.cameras[cam].show()
            self.cameras[cam].resize(240 , 138)
            self.cameras[cam].move( 10+240*(cidx%6) , 10+140*(cidx//6))
        listwidget = self.ui.cmr_listWidget
        items =  [listwidget.item(i) for i in range(listwidget.count())]
        for item in items:
            item.setBackground( QColor(0,200,0) )
        listwidget = self.ui.cmr_listWidget_3
        items =  [listwidget.item(i) for i in range(listwidget.count())]
        for item in items:
            item.setBackground( QColor(0,200,0) )
        listwidget = self.ui.cmr_listWidget_4
        items =  [listwidget.item(i) for i in range(listwidget.count())]
        for item in items:
            item.setBackground( QColor(0,200,0) )

    def showLayer1(self):
        self.currentLayer = 1
        self.setlistcolors()
        self.changelistColor()
        w0 = 480
        h0 = 280
        l = [
            [0 , 0 , w0*2 , h0*2],
            [w0*2 , h0*0 , w0*3 , h0*1],
            [w0*2 , h0*1 , w0*3 , h0*2],
            [w0*0 , h0*2 , w0*1 , h0*3],
            [w0*1 , h0*2 , w0*2 , h0*3],
            [w0*2 , h0*2 , w0*3 , h0*3],
        ]
        for cam in self.cameras:
            self.cameras[cam].hide()
            self.cameras[cam].active = False
        for cidx  , cam in enumerate(self.layers["6"]):
            cam.active=True
            cam.show()
            if cidx == 0:
                x = l[cidx][0]
                y = l[cidx][1]
                w = l[cidx][2] - l[cidx][0]
                h = l[cidx][3] - l[cidx][1]
                cam.move(10,10)
                cam.resize(w,h)
            else:
                x = l[cidx][0]
                y = l[cidx][1]
                cam.move(x+10,y+10)
                cam.resize(w0,h0)

    def showLayer2(self):
        self.currentLayer = 2
        self.setlistcolors()
        self.changelistColor()
        w0 = 1440/4
        h0 = 840/4
        l = [
            [0 , 0 , w0*3 , h0*3],

            [w0*3 , h0*0 , w0*4 , h0*1],
            [w0*3 , h0*1 , w0*4 , h0*2],
            [w0*3 , h0*2 , w0*4 , h0*3],

            [w0*0 , h0*3 , w0*1 , h0*4],
            [w0*1 , h0*3 , w0*2 , h0*4],
            [w0*2 , h0*3 , w0*3 , h0*4],
            [w0*3 , h0*3 , w0*4 , h0*4],
        ]
        for cam in self.cameras:
            self.cameras[cam].hide()
            self.cameras[cam].active = False
        for cidx  , cam in enumerate(self.layers["7_1"]):
            cam.show()
            cam.active = True
            x = l[cidx][0]
            y = l[cidx][1]
            w = l[cidx][2] - l[cidx][0]
            h = l[cidx][3] - l[cidx][1]
            cam.move(x+10,y+10)
            cam.resize(w,h)      

    def showLayer3(self):
        self.currentLayer = 3
        self.setlistcolors()
        self.changelistColor()
        w0 = 1440/4
        h0 = 840/4
        l = [
            [0 , 0 , w0*2 , h0*2],
            [w0*2 , h0*0 , w0*4 , h0*2],

            [w0*0 , h0*2 , w0*1 , h0*3],
            [w0*1 , h0*2 , w0*2 , h0*3],

            [w0*2 , h0*2 , w0*4 , h0*4],

            [w0*0 , h0*3 , w0*1 , h0*4],
            [w0*1 , h0*3 , w0*2 , h0*4],
        ]
        for cam in self.cameras:
            self.cameras[cam].hide()
            self.cameras[cam].active = False
        for cidx  , cam in enumerate(self.layers["7_2"]):
            cam.show()
            cam.active = True
            x = l[cidx][0]
            y = l[cidx][1]
            w = l[cidx][2] - l[cidx][0]
            h = l[cidx][3] - l[cidx][1]
            cam.move(x+10,y+10)
            cam.resize(w,h)      

    def showLayer4(self):
        self.currentLayer = 4
        self.setlistcolors()
        self.changelistColor()
        w0 = 1440/4
        h0 = 840/4
        l = [
            [0 , 0 , w0*2 , h0*2],
            [w0*2 , h0*0 , w0*4 , h0*2],

            [w0*0 , h0*2 , w0*1 , h0*3],
            [w0*1 , h0*2 , w0*2 , h0*3],
            [w0*2 , h0*2 , w0*3 , h0*3],
            [w0*3 , h0*2 , w0*4 , h0*3],

            [w0*0 , h0*3 , w0*1 , h0*4],
            [w0*1 , h0*3 , w0*2 , h0*4],
            [w0*2 , h0*3 , w0*3 , h0*4],
            [w0*3 , h0*3 , w0*4 , h0*4],
        ]

        for cam in self.cameras:
            self.cameras[cam].hide()
            self.cameras[cam].active = False
        for cidx  , cam in enumerate(self.layers["10"]):
            cam.show()
            cam.active = True
            x = l[cidx][0]
            y = l[cidx][1]
            w = l[cidx][2] - l[cidx][0]
            h = l[cidx][3] - l[cidx][1]
            cam.move(x+10,y+10)
            cam.resize(w,h)  

    def showLayer5(self):
        self.currentLayer = 5
        self.setlistcolors()
        self.changelistColor()
        w0 = 1440/4
        h0 = 840/4
        l = [
            [0 , 0 , w0*2 , h0*2],  
            [w0*2 , h0*0 , w0*3 , h0*1],
            [w0*3 , h0*0 , w0*4 , h0*1],

            [w0*2 , h0*1 , w0*3 , h0*2],
            [w0*3 , h0*1 , w0*4 , h0*2],

            [w0*0 , h0*2 , w0*1 , h0*3],
            [w0*1 , h0*2 , w0*2 , h0*3],
            [w0*2 , h0*2 , w0*3 , h0*3],
            [w0*3 , h0*2 , w0*4 , h0*3],

            [w0*0 , h0*3 , w0*1 , h0*4],
            [w0*1 , h0*3 , w0*2 , h0*4],
            [w0*2 , h0*3 , w0*3 , h0*4],
            [w0*3 , h0*3 , w0*4 , h0*4],
        ]
        for cam in self.cameras:
            self.cameras[cam].hide()
            self.cameras[cam].active = False
        for cidx  , cam in enumerate(self.layers["13"]):
            cam.show()
            cam.active = True
            x = l[cidx][0]
            y = l[cidx][1]
            w = l[cidx][2] - l[cidx][0]
            h = l[cidx][3] - l[cidx][1]
            cam.move(x+10,y+10)
            cam.resize(w,h) 

    def resizeCamers(self,cam ,camera):
        if camera.full:
            camera.full = False
            for cam_ in self.cameras:
                self.cameras[cam_].hide()
            self.fullscreens[self.currentLayer]()
            self.settingLayer.hide()
        else:
            camera.full = True
            for cam_ in self.cameras:
                if cam != cam_:
                    self.cameras[cam_].hide()
            camera.resize(1491 , 891)
            camera.move(10,10)
            self.settingLayer.show()



    def fullscreen01(self):
        cam  =self.currentCam = 'cam01'
        camera = self.cameras[cam]
        self.loadCameraSet()
        self.setLayerCorlr()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            self.resizeCamers(cam ,camera )
        self.dclickTime[1] = time.time()
        

    def fullscreen02(self):
        cam  =self.currentCam = 'cam02'
        camera = self.cameras[cam]
        self.loadCameraSet()
        self.setLayerCorlr()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            self.resizeCamers(cam ,camera )
        self.dclickTime[1] = time.time()


    def fullscreen03(self):
            cam  =self.currentCam = 'cam03'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen04(self):
            cam  =self.currentCam = 'cam04'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen05(self):
            cam  =self.currentCam = 'cam05'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen06(self):
            cam  =self.currentCam = 'cam06'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen07(self):
            cam  =self.currentCam = 'cam07'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen08(self):
            cam  =self.currentCam = 'cam08'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen09(self):
            cam  =self.currentCam = 'cam09'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen10(self):
            cam  =self.currentCam = 'cam10'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen11(self):
            cam  =self.currentCam = 'cam11'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen12(self):
            cam  =self.currentCam = 'cam12'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen13(self):
            cam  =self.currentCam = 'cam13'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen14(self):
            cam  =self.currentCam = 'cam14'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen15(self):
            cam  =self.currentCam = 'cam15'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen16(self):
            cam  =self.currentCam = 'cam16'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen17(self):
            cam  =self.currentCam = 'cam17'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen18(self):
            cam  =self.currentCam = 'cam18'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen19(self):
            cam  =self.currentCam = 'cam19'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen20(self):
            cam  =self.currentCam = 'cam20'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen21(self):
            cam  =self.currentCam = 'cam21'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen22(self):
            cam  =self.currentCam = 'cam22'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen23(self):
            cam  =self.currentCam = 'cam23'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen24(self):
            cam  =self.currentCam = 'cam24'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen25(self):
            cam  =self.currentCam = 'cam25'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen26(self):
            cam  =self.currentCam = 'cam26'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen27(self):
            cam  =self.currentCam = 'cam27'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen28(self):
            cam  =self.currentCam = 'cam28'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen29(self):
            cam  =self.currentCam = 'cam29'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen30(self):
            cam  =self.currentCam = 'cam30'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen31(self):
            cam  =self.currentCam = 'cam31'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


    def fullscreen32(self):
            cam  =self.currentCam = 'cam32'
            camera = self.cameras[cam]
            self.loadCameraSet()
            self.setLayerCorlr()
            now = time.time()
            if now - self.dclickTime[1]  < 0.3:
                self.resizeCamers(cam ,camera )
            self.dclickTime[1] = time.time()


