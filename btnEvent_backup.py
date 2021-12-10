import time
import copy
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
            self.ui.cmraBt_21
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
 
      
    def fullscreen01(self):
        self.currentCam = 'cam01'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_01.size().width() == 240:
                self.ui.cmraBt_01.resize(1491 , 891)
                self.ui.cmraBt_01.move(10,10)
                for i in range(1,33):
                    if i == 1 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_01.resize(240 , 138)
                self.ui.cmraBt_01.move(10,10)
                for i in range(1,33):
                    if i == 1 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
        

    def fullscreen02(self):
        self.currentCam = 'cam02'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_02.size().width() == 240:
                self.ui.cmraBt_02.resize(1491 , 891)
                self.ui.cmraBt_02.move(10,10)
                for i in range(1,33):
                    if i == 2 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_02.resize(240 , 138)
                self.ui.cmraBt_02.move(10+240*1,10)
                for i in range(1,33):
                    if i == 2 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()


    def fullscreen03(self):
        self.currentCam = 'cam03'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_03.size().width() == 240:
                self.ui.cmraBt_03.resize(1491 , 891)
                self.ui.cmraBt_03.move(10,10)
                for i in range(1,33):
                    if i == 3 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_03.resize(240 , 138)
                self.ui.cmraBt_03.move(10+240*2,10)
                for i in range(1,33):
                    if i == 3 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    
    def fullscreen04(self):
        self.currentCam = 'cam04'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_04.size().width() == 240:
                self.ui.cmraBt_04.resize(1491 , 891)
                self.ui.cmraBt_04.move(10,10)
                for i in range(1,33):
                    if i == 4 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_04.resize(240 , 138)
                self.ui.cmraBt_04.move(10+240*3,10)
                for i in range(1,33):
                    if i == 4 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()

    def fullscreen05(self):
        self.currentCam = 'cam05'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_05.size().width() == 240:
                self.ui.cmraBt_05.resize(1491 , 891)
                self.ui.cmraBt_05.move(10,10)
                for i in range(1,33):
                    if i == 5 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_05.resize(240 , 138)
                self.ui.cmraBt_05.move(10+240*4,10)
                for i in range(1,33):
                    if i == 5 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    
    def fullscreen06(self):
        self.currentCam = 'cam06'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_06.size().width() == 240:
                self.ui.cmraBt_06.resize(1491 , 891)
                self.ui.cmraBt_06.move(10,10)
                for i in range(1,33):
                    if i == 6 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_06.resize(240 , 138)
                self.ui.cmraBt_06.move(10+240*5,10)
                for i in range(1,33):
                    if i == 6 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    
    def fullscreen07(self):
        self.currentCam = 'cam07'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_07.size().width() == 240:
                self.ui.cmraBt_07.resize(1491 , 891)
                self.ui.cmraBt_07.move(10,10)
                for i in range(1,33):
                    if i == 7 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_07.resize(240 , 138)
                self.ui.cmraBt_07.move(10+240*0,10+140*1)
                for i in range(1,33):
                    if i == 7 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    
    def fullscreen08(self):
        self.currentCam = 'cam08'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_08.size().width() == 240:
                self.ui.cmraBt_08.resize(1491 , 891)
                self.ui.cmraBt_08.move(10,10)
                for i in range(1,33):
                    if i == 8 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_08.resize(240 , 138)
                self.ui.cmraBt_08.move(10+240*1,10+140*1)
                for i in range(1,33):
                    if i == 8 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    
    def fullscreen09(self):
        self.currentCam = 'cam09'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_09.size().width() == 240:
                self.ui.cmraBt_09.resize(1491 , 891)
                self.ui.cmraBt_09.move(10,10)
                for i in range(1,33):
                    if i == 9 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_09.resize(240 , 138)
                self.ui.cmraBt_09.move(10+240*2,10+140*1)
                for i in range(1,33):
                    if i == 9 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    
    def fullscreen10(self):
        self.currentCam = 'cam10'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_10.size().width() == 240:
                self.ui.cmraBt_10.resize(1491 , 891)
                self.ui.cmraBt_10.move(10,10)
                for i in range(1,33):
                    if i == 10 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_10.resize(240 , 138)
                self.ui.cmraBt_10.move(10+240*3,10+140*1)
                for i in range(1,33):
                    if i == 10 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    

    def fullscreen11(self):
        self.currentCam = 'cam11'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_11.size().width() == 240:
                self.ui.cmraBt_11.resize(1491 , 891)
                self.ui.cmraBt_11.move(10,10)
                for i in range(1,33):
                    if i == 11 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_11.resize(240 , 138)
                self.ui.cmraBt_11.move(10+240*4,10+140*1)
                for i in range(1,33):
                    if i == 11 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()

    def fullscreen12(self):
        self.currentCam = 'cam12'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_12.size().width() == 240:
                self.ui.cmraBt_12.resize(1491 , 891)
                self.ui.cmraBt_12.move(10,10)
                for i in range(1,33):
                    if i == 12 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_12.resize(240 , 138)
                self.ui.cmraBt_12.move(10+240*5,10+140*1)
                for i in range(1,33):
                    if i == 12 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    
    def fullscreen13(self):
        self.currentCam = 'cam13'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_13.size().width() == 240:
                self.ui.cmraBt_13.resize(1491 , 891)
                self.ui.cmraBt_13.move(10,10)
                for i in range(1,33):
                    if i == 13 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_13.resize(240 , 138)
                self.ui.cmraBt_13.move(10+240*0,10+140*2)
                for i in range(1,33):
                    if i == 13 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    
    def fullscreen14(self):
        self.currentCam = 'cam14'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_14.size().width() == 240:
                self.ui.cmraBt_14.resize(1491 , 891)
                self.ui.cmraBt_14.move(10,10)
                for i in range(1,33):
                    if i == 14 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_14.resize(240 , 138)
                self.ui.cmraBt_14.move(10+240*1,10+140*2)
                for i in range(1,33):
                    if i == 14 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    
    def fullscreen15(self):
        self.currentCam = 'cam15'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_15.size().width() == 240:
                self.ui.cmraBt_15.resize(1491 , 891)
                self.ui.cmraBt_15.move(10,10)
                for i in range(1,33):
                    if i == 15 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_15.resize(240 , 138)
                self.ui.cmraBt_15.move(10+240*2,10+140*2)
                for i in range(1,33):
                    if i == 15 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    
    def fullscreen16(self):
        self.currentCam = 'cam16'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_16.size().width() == 240:
                self.ui.cmraBt_16.resize(1491 , 891)
                self.ui.cmraBt_16.move(10,10)
                for i in range(1,33):
                    if i == 16 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_16.resize(240 , 138)
                self.ui.cmraBt_16.move(10+240*3,10+140*2)
                for i in range(1,33):
                    if i == 16 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    
    def fullscreen17(self):
        self.currentCam = 'cam17'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_17.size().width() == 240:
                self.ui.cmraBt_17.resize(1491 , 891)
                self.ui.cmraBt_17.move(10,10)
                for i in range(1,33):
                    if i == 17 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_17.resize(240 , 138)
                self.ui.cmraBt_17.move(10+240*4,10+140*2)
                for i in range(1,33):
                    if i == 17 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    
    def fullscreen18(self):
        self.currentCam = 'cam18'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_18.size().width() == 240:
                self.ui.cmraBt_18.resize(1491 , 891)
                self.ui.cmraBt_18.move(10,10)
                for i in range(1,33):
                    if i == 18 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_18.resize(240 , 138)
                self.ui.cmraBt_18.move(10+240*5,10+140*2)
                for i in range(1,33):
                    if i == 18 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    
    def fullscreen19(self):
        self.currentCam = 'cam19'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_19.size().width() == 240:
                self.ui.cmraBt_19.resize(1491 , 891)
                self.ui.cmraBt_19.move(10,10)
                for i in range(1,33):
                    if i == 19 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_19.resize(240 , 138)
                self.ui.cmraBt_19.move(10+240*0,10+140*3)
                for i in range(1,33):
                    if i == 19 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    
    def fullscreen20(self):
        self.currentCam = 'cam20'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_20.size().width() == 240:
                self.ui.cmraBt_20.resize(1491 , 891)
                self.ui.cmraBt_20.move(10,10)
                for i in range(1,33):
                    if i == 20 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_20.resize(240 , 138)
                self.ui.cmraBt_20.move(10+240*1,10+140*3)
                for i in range(1,33):
                    if i == 20 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    
    def fullscreen21(self):
        self.currentCam = 'cam21'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_21.size().width() == 240:
                self.ui.cmraBt_21.resize(1491 , 891)
                self.ui.cmraBt_21.move(10,10)
                for i in range(1,33):
                    if i == 21 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_21.resize(240 , 138)
                self.ui.cmraBt_21.move(10+240*2,10+140*3)
                for i in range(1,33):
                    if i == 21 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    
    def fullscreen22(self):
        self.currentCam = 'cam22'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_22.size().width() == 240:
                self.ui.cmraBt_22.resize(1491 , 891)
                self.ui.cmraBt_22.move(10,10)
                for i in range(1,33):
                    if i == 22 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_22.resize(240 , 138)
                self.ui.cmraBt_22.move(10+240*3,10+140*3)
                for i in range(1,33):
                    if i == 22 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    
    def fullscreen23(self):
        self.currentCam = 'cam23'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_23.size().width() == 240:
                self.ui.cmraBt_23.resize(1491 , 891)
                self.ui.cmraBt_23.move(10,10)
                for i in range(1,33):
                    if i == 23 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_23.resize(240 , 138)
                self.ui.cmraBt_23.move(10+240*4,10+140*3)
                for i in range(1,33):
                    if i == 23 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    
    def fullscreen24(self):
        self.currentCam = 'cam24'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_24.size().width() == 240:
                self.ui.cmraBt_24.resize(1491 , 891)
                self.ui.cmraBt_24.move(10,10)
                for i in range(1,33):
                    if i == 24 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_24.resize(240 , 138)
                self.ui.cmraBt_24.move(10+240*5,10+140*3)
                for i in range(1,33):
                    if i == 24 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    
    def fullscreen25(self):
        self.currentCam = 'cam25'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_25.size().width() == 240:
                self.ui.cmraBt_25.resize(1491 , 891)
                self.ui.cmraBt_25.move(10,10)
                for i in range(1,33):
                    if i == 25 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_25.resize(240 , 138)
                self.ui.cmraBt_25.move(10+240*0,10+140*4)
                for i in range(1,33):
                    if i == 25 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    
    def fullscreen26(self):
        self.currentCam = 'cam26'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_26.size().width() == 240:
                self.ui.cmraBt_26.resize(1491 , 891)
                self.ui.cmraBt_26.move(10,10)
                for i in range(1,33):
                    if i == 26 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_26.resize(240 , 138)
                self.ui.cmraBt_26.move(10+240*1,10+140*4)
                for i in range(1,33):
                    if i == 26 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    
    def fullscreen27(self):
        self.currentCam = 'cam27'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_27.size().width() == 240:
                self.ui.cmraBt_27.resize(1491 , 891)
                self.ui.cmraBt_27.move(10,10)
                for i in range(1,33):
                    if i == 27 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_27.resize(240 , 138)
                self.ui.cmraBt_27.move(10+240*2,10+140*4)
                for i in range(1,33):
                    if i == 27 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    
    def fullscreen28(self):
        self.currentCam = 'cam28'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_28.size().width() == 240:
                self.ui.cmraBt_28.resize(1491 , 891)
                self.ui.cmraBt_28.move(10,10)
                for i in range(1,33):
                    if i == 28 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_28.resize(240 , 138)
                self.ui.cmraBt_28.move(10+240*3,10+140*4)
                for i in range(1,33):
                    if i == 28 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    
    def fullscreen29(self):
        self.currentCam = 'cam29'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_29.size().width() == 240:
                self.ui.cmraBt_29.resize(1491 , 891)
                self.ui.cmraBt_29.move(10,10)
                for i in range(1,33):
                    if i == 29 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_29.resize(240 , 138)
                self.ui.cmraBt_29.move(10+240*4,10+140*4)
                for i in range(1,33):
                    if i == 29 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    
    def fullscreen30(self):
        self.currentCam = 'cam30'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_30.size().width() == 240:
                self.ui.cmraBt_30.resize(1491 , 891)
                self.ui.cmraBt_30.move(10,10)
                for i in range(1,33):
                    if i == 30 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_30.resize(240 , 138)
                self.ui.cmraBt_30.move(10+240*5,10+140*4)
                for i in range(1,33):
                    if i == 30 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    
    def fullscreen31(self):
        self.currentCam = 'cam31'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_31.size().width() == 240:
                self.ui.cmraBt_31.resize(1491 , 891)
                self.ui.cmraBt_31.move(10,10)
                for i in range(1,33):
                    if i == 31 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_31.resize(240 , 138)
                self.ui.cmraBt_31.move(10+240*0,10+140*5)
                for i in range(1,33):
                    if i == 31 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()

    def fullscreen32(self):
        self.currentCam = 'cam32'
        self.loadCameraSet()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            if self.ui.cmraBt_32.size().width() == 240:
                self.ui.cmraBt_32.resize(1491 , 891)
                self.ui.cmraBt_32.move(10,10)
                for i in range(1,33):
                    if i == 32 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.hide()'%i)
                self.settingLayer.show()
            else:
                self.ui.cmraBt_32.resize(240 , 138)
                self.ui.cmraBt_32.move(10+240*0,10+140*5)
                for i in range(1,33):
                    if i == 32 :
                        pass
                    else :
                        exec('self.ui.cmraBt_%02d.show()'%i)
                self.settingLayer.hide()
        self.dclickTime[1] = time.time()
    

