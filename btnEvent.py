import time

class btns():
    def __init__(self , parent):
        self.parent = parent
    
    def dclickEvents(self):
        self.parent.fullscreen01 = self.fullscreen01
        self.parent.ui.cmraBt_01.clicked.connect(self.parent.fullscreen01)
        self.parent.fullscreen02 = self.fullscreen02
        self.parent.ui.cmraBt_02.clicked.connect(self.parent.fullscreen02)
        self.parent.fullscreen03 = self.fullscreen03
        self.parent.ui.cmraBt_03.clicked.connect(self.parent.fullscreen03)
        self.parent.fullscreen04 = self.fullscreen04
        self.parent.ui.cmraBt_04.clicked.connect(self.parent.fullscreen04)
        self.parent.fullscreen05 = self.fullscreen05
        self.parent.ui.cmraBt_05.clicked.connect(self.parent.fullscreen05)
        self.parent.fullscreen06 = self.fullscreen06
        self.parent.ui.cmraBt_06.clicked.connect(self.parent.fullscreen06)
        self.parent.fullscreen07 = self.fullscreen07
        self.parent.ui.cmraBt_07.clicked.connect(self.parent.fullscreen07)
        self.parent.fullscreen08 = self.fullscreen08
        self.parent.ui.cmraBt_08.clicked.connect(self.parent.fullscreen08)
        self.parent.fullscreen09 = self.fullscreen09
        self.parent.ui.cmraBt_09.clicked.connect(self.parent.fullscreen09)
        self.parent.fullscreen10 = self.fullscreen10
        self.parent.ui.cmraBt_10.clicked.connect(self.parent.fullscreen10)
        self.parent.fullscreen11 = self.fullscreen11
        self.parent.ui.cmraBt_11.clicked.connect(self.parent.fullscreen11)
        self.parent.fullscreen12 = self.fullscreen12
        self.parent.ui.cmraBt_12.clicked.connect(self.parent.fullscreen12)
        self.parent.fullscreen13 = self.fullscreen13
        self.parent.ui.cmraBt_13.clicked.connect(self.parent.fullscreen13)
        self.parent.fullscreen14 = self.fullscreen14
        self.parent.ui.cmraBt_14.clicked.connect(self.parent.fullscreen14)
        self.parent.fullscreen15 = self.fullscreen15
        self.parent.ui.cmraBt_15.clicked.connect(self.parent.fullscreen15)
        self.parent.fullscreen16 = self.fullscreen16
        self.parent.ui.cmraBt_16.clicked.connect(self.parent.fullscreen16)
        self.parent.fullscreen17 = self.fullscreen17
        self.parent.ui.cmraBt_17.clicked.connect(self.parent.fullscreen17)
        self.parent.fullscreen18 = self.fullscreen18
        self.parent.ui.cmraBt_18.clicked.connect(self.parent.fullscreen18)
        self.parent.fullscreen19 = self.fullscreen19
        self.parent.ui.cmraBt_19.clicked.connect(self.parent.fullscreen19)
        self.parent.fullscreen20 = self.fullscreen20
        self.parent.ui.cmraBt_20.clicked.connect(self.parent.fullscreen20)
        self.parent.fullscreen21 = self.fullscreen21
        self.parent.ui.cmraBt_21.clicked.connect(self.parent.fullscreen21)
        self.parent.fullscreen22 = self.fullscreen22
        self.parent.ui.cmraBt_22.clicked.connect(self.parent.fullscreen22)
        self.parent.fullscreen23 = self.fullscreen23
        self.parent.ui.cmraBt_23.clicked.connect(self.parent.fullscreen23)
        self.parent.fullscreen24 = self.fullscreen24
        self.parent.ui.cmraBt_24.clicked.connect(self.parent.fullscreen24)
        self.parent.fullscreen25 = self.fullscreen25
        self.parent.ui.cmraBt_25.clicked.connect(self.parent.fullscreen25)
        self.parent.fullscreen26 = self.fullscreen26
        self.parent.ui.cmraBt_26.clicked.connect(self.parent.fullscreen26)
        self.parent.fullscreen27 = self.fullscreen27
        self.parent.ui.cmraBt_27.clicked.connect(self.parent.fullscreen27)
        self.parent.fullscreen28 = self.fullscreen28
        self.parent.ui.cmraBt_28.clicked.connect(self.parent.fullscreen28)
        self.parent.fullscreen29 = self.fullscreen29
        self.parent.ui.cmraBt_29.clicked.connect(self.parent.fullscreen29)
        self.parent.fullscreen30 = self.fullscreen30
        self.parent.ui.cmraBt_30.clicked.connect(self.parent.fullscreen30)
        self.parent.fullscreen31 = self.fullscreen31
        self.parent.ui.cmraBt_31.clicked.connect(self.parent.fullscreen31)
        self.parent.fullscreen32 = self.fullscreen32
        self.parent.ui.cmraBt_32.clicked.connect(self.parent.fullscreen32)
        self.parent.fullscreen33 = self.fullscreen33
        self.parent.ui.cmraBt_33.clicked.connect(self.parent.fullscreen33)
        self.parent.fullscreen34 = self.fullscreen34
        self.parent.ui.cmraBt_34.clicked.connect(self.parent.fullscreen34)
        self.parent.fullscreen35 = self.fullscreen35
        self.parent.ui.cmraBt_35.clicked.connect(self.parent.fullscreen35)
        self.parent.fullscreen36 = self.fullscreen36
        self.parent.ui.cmraBt_36.clicked.connect(self.parent.fullscreen36)       
      
    def fullscreen01(self):
        print("ok")
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_01.size().width() == 240:
                self.parent.ui.cmraBt_01.resize(1491 , 891)
                self.parent.ui.cmraBt_01.move(10,10)
                for i in range(1,37):
                    if i == 1 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_01.resize(240 , 138)
                self.parent.ui.cmraBt_01.move(10,10)
                for i in range(1,37):
                    if i == 1 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()

    def fullscreen02(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_02.size().width() == 240:
                self.parent.ui.cmraBt_02.resize(1491 , 891)
                self.parent.ui.cmraBt_02.move(10,10)
                for i in range(1,37):
                    if i == 2 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_02.resize(240 , 138)
                self.parent.ui.cmraBt_02.move(10+240*1,10)
                for i in range(1,37):
                    if i == 2 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()


    def fullscreen03(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_03.size().width() == 240:
                self.parent.ui.cmraBt_03.resize(1491 , 891)
                self.parent.ui.cmraBt_03.move(10,10)
                for i in range(1,37):
                    if i == 3 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_03.resize(240 , 138)
                self.parent.ui.cmraBt_03.move(10+240*2,10)
                for i in range(1,37):
                    if i == 3 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen04(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_04.size().width() == 240:
                self.parent.ui.cmraBt_04.resize(1491 , 891)
                self.parent.ui.cmraBt_04.move(10,10)
                for i in range(1,37):
                    if i == 4 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_04.resize(240 , 138)
                self.parent.ui.cmraBt_04.move(10+240*3,10)
                for i in range(1,37):
                    if i == 4 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()

    def fullscreen05(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_05.size().width() == 240:
                self.parent.ui.cmraBt_05.resize(1491 , 891)
                self.parent.ui.cmraBt_05.move(10,10)
                for i in range(1,37):
                    if i == 5 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_05.resize(240 , 138)
                self.parent.ui.cmraBt_05.move(10+240*4,10)
                for i in range(1,37):
                    if i == 5 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen06(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_06.size().width() == 240:
                self.parent.ui.cmraBt_06.resize(1491 , 891)
                self.parent.ui.cmraBt_06.move(10,10)
                for i in range(1,37):
                    if i == 6 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_06.resize(240 , 138)
                self.parent.ui.cmraBt_06.move(10+240*5,10)
                for i in range(1,37):
                    if i == 6 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen07(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_07.size().width() == 240:
                self.parent.ui.cmraBt_07.resize(1491 , 891)
                self.parent.ui.cmraBt_07.move(10,10)
                for i in range(1,37):
                    if i == 7 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_07.resize(240 , 138)
                self.parent.ui.cmraBt_07.move(10+240*0,10+140*1)
                for i in range(1,37):
                    if i == 7 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen08(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_08.size().width() == 240:
                self.parent.ui.cmraBt_08.resize(1491 , 891)
                self.parent.ui.cmraBt_08.move(10,10)
                for i in range(1,37):
                    if i == 8 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_08.resize(240 , 138)
                self.parent.ui.cmraBt_08.move(10+240*1,10+140*1)
                for i in range(1,37):
                    if i == 8 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen09(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_09.size().width() == 240:
                self.parent.ui.cmraBt_09.resize(1491 , 891)
                self.parent.ui.cmraBt_09.move(10,10)
                for i in range(1,37):
                    if i == 9 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_09.resize(240 , 138)
                self.parent.ui.cmraBt_09.move(10+240*2,10+140*1)
                for i in range(1,37):
                    if i == 9 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen10(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_10.size().width() == 240:
                self.parent.ui.cmraBt_10.resize(1491 , 891)
                self.parent.ui.cmraBt_10.move(10,10)
                for i in range(1,37):
                    if i == 10 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_10.resize(240 , 138)
                self.parent.ui.cmraBt_10.move(10+240*3,10+140*1)
                for i in range(1,37):
                    if i == 10 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    

    def fullscreen11(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_11.size().width() == 240:
                self.parent.ui.cmraBt_11.resize(1491 , 891)
                self.parent.ui.cmraBt_11.move(10,10)
                for i in range(1,37):
                    if i == 11 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_11.resize(240 , 138)
                self.parent.ui.cmraBt_11.move(10+240*4,10+140*1)
                for i in range(1,37):
                    if i == 11 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()

    def fullscreen12(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_12.size().width() == 240:
                self.parent.ui.cmraBt_12.resize(1491 , 891)
                self.parent.ui.cmraBt_12.move(10,10)
                for i in range(1,37):
                    if i == 12 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_12.resize(240 , 138)
                self.parent.ui.cmraBt_12.move(10+240*5,10+140*1)
                for i in range(1,37):
                    if i == 12 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen13(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_13.size().width() == 240:
                self.parent.ui.cmraBt_13.resize(1491 , 891)
                self.parent.ui.cmraBt_13.move(10,10)
                for i in range(1,37):
                    if i == 13 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_13.resize(240 , 138)
                self.parent.ui.cmraBt_13.move(10+240*0,10+140*2)
                for i in range(1,37):
                    if i == 13 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen14(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_14.size().width() == 240:
                self.parent.ui.cmraBt_14.resize(1491 , 891)
                self.parent.ui.cmraBt_14.move(10,10)
                for i in range(1,37):
                    if i == 14 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_14.resize(240 , 138)
                self.parent.ui.cmraBt_14.move(10+240*1,10+140*2)
                for i in range(1,37):
                    if i == 14 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen15(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_15.size().width() == 240:
                self.parent.ui.cmraBt_15.resize(1491 , 891)
                self.parent.ui.cmraBt_15.move(10,10)
                for i in range(1,37):
                    if i == 15 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_15.resize(240 , 138)
                self.parent.ui.cmraBt_15.move(10+240*2,10+140*2)
                for i in range(1,37):
                    if i == 15 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen16(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_16.size().width() == 240:
                self.parent.ui.cmraBt_16.resize(1491 , 891)
                self.parent.ui.cmraBt_16.move(10,10)
                for i in range(1,37):
                    if i == 16 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_16.resize(240 , 138)
                self.parent.ui.cmraBt_16.move(10+240*3,10+140*2)
                for i in range(1,37):
                    if i == 16 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen17(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_17.size().width() == 240:
                self.parent.ui.cmraBt_17.resize(1491 , 891)
                self.parent.ui.cmraBt_17.move(10,10)
                for i in range(1,37):
                    if i == 17 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_17.resize(240 , 138)
                self.parent.ui.cmraBt_17.move(10+240*4,10+140*2)
                for i in range(1,37):
                    if i == 17 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen18(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_18.size().width() == 240:
                self.parent.ui.cmraBt_18.resize(1491 , 891)
                self.parent.ui.cmraBt_18.move(10,10)
                for i in range(1,37):
                    if i == 18 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_18.resize(240 , 138)
                self.parent.ui.cmraBt_18.move(10+240*5,10+140*2)
                for i in range(1,37):
                    if i == 18 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen19(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_19.size().width() == 240:
                self.parent.ui.cmraBt_19.resize(1491 , 891)
                self.parent.ui.cmraBt_19.move(10,10)
                for i in range(1,37):
                    if i == 19 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_19.resize(240 , 138)
                self.parent.ui.cmraBt_19.move(10+240*0,10+140*3)
                for i in range(1,37):
                    if i == 19 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen20(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_20.size().width() == 240:
                self.parent.ui.cmraBt_20.resize(1491 , 891)
                self.parent.ui.cmraBt_20.move(10,10)
                for i in range(1,37):
                    if i == 20 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_20.resize(240 , 138)
                self.parent.ui.cmraBt_20.move(10+240*1,10+140*3)
                for i in range(1,37):
                    if i == 20 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen21(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_21.size().width() == 240:
                self.parent.ui.cmraBt_21.resize(1491 , 891)
                self.parent.ui.cmraBt_21.move(10,10)
                for i in range(1,37):
                    if i == 21 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_21.resize(240 , 138)
                self.parent.ui.cmraBt_21.move(10+240*2,10+140*3)
                for i in range(1,37):
                    if i == 21 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen22(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_22.size().width() == 240:
                self.parent.ui.cmraBt_22.resize(1491 , 891)
                self.parent.ui.cmraBt_22.move(10,10)
                for i in range(1,37):
                    if i == 22 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_22.resize(240 , 138)
                self.parent.ui.cmraBt_22.move(10+240*3,10+140*3)
                for i in range(1,37):
                    if i == 22 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen23(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_23.size().width() == 240:
                self.parent.ui.cmraBt_23.resize(1491 , 891)
                self.parent.ui.cmraBt_23.move(10,10)
                for i in range(1,37):
                    if i == 23 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_23.resize(240 , 138)
                self.parent.ui.cmraBt_23.move(10+240*4,10+140*3)
                for i in range(1,37):
                    if i == 23 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen24(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_24.size().width() == 240:
                self.parent.ui.cmraBt_24.resize(1491 , 891)
                self.parent.ui.cmraBt_24.move(10,10)
                for i in range(1,37):
                    if i == 24 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_24.resize(240 , 138)
                self.parent.ui.cmraBt_24.move(10+240*5,10+140*3)
                for i in range(1,37):
                    if i == 24 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen25(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_25.size().width() == 240:
                self.parent.ui.cmraBt_25.resize(1491 , 891)
                self.parent.ui.cmraBt_25.move(10,10)
                for i in range(1,37):
                    if i == 25 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_25.resize(240 , 138)
                self.parent.ui.cmraBt_25.move(10+240*0,10+140*4)
                for i in range(1,37):
                    if i == 25 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen26(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_26.size().width() == 240:
                self.parent.ui.cmraBt_26.resize(1491 , 891)
                self.parent.ui.cmraBt_26.move(10,10)
                for i in range(1,37):
                    if i == 26 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_26.resize(240 , 138)
                self.parent.ui.cmraBt_26.move(10+240*1,10+140*4)
                for i in range(1,37):
                    if i == 26 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen27(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_27.size().width() == 240:
                self.parent.ui.cmraBt_27.resize(1491 , 891)
                self.parent.ui.cmraBt_27.move(10,10)
                for i in range(1,37):
                    if i == 27 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_27.resize(240 , 138)
                self.parent.ui.cmraBt_27.move(10+240*2,10+140*4)
                for i in range(1,37):
                    if i == 27 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen28(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_28.size().width() == 240:
                self.parent.ui.cmraBt_28.resize(1491 , 891)
                self.parent.ui.cmraBt_28.move(10,10)
                for i in range(1,37):
                    if i == 28 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_28.resize(240 , 138)
                self.parent.ui.cmraBt_28.move(10+240*3,10+140*4)
                for i in range(1,37):
                    if i == 28 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen29(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_29.size().width() == 240:
                self.parent.ui.cmraBt_29.resize(1491 , 891)
                self.parent.ui.cmraBt_29.move(10,10)
                for i in range(1,37):
                    if i == 29 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_29.resize(240 , 138)
                self.parent.ui.cmraBt_29.move(10+240*4,10+140*4)
                for i in range(1,37):
                    if i == 29 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen30(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_30.size().width() == 240:
                self.parent.ui.cmraBt_30.resize(1491 , 891)
                self.parent.ui.cmraBt_30.move(10,10)
                for i in range(1,37):
                    if i == 30 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_30.resize(240 , 138)
                self.parent.ui.cmraBt_30.move(10+240*5,10+140*4)
                for i in range(1,37):
                    if i == 30 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen31(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_31.size().width() == 240:
                self.parent.ui.cmraBt_31.resize(1491 , 891)
                self.parent.ui.cmraBt_31.move(10,10)
                for i in range(1,37):
                    if i == 31 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_31.resize(240 , 138)
                self.parent.ui.cmraBt_31.move(10+240*0,10+140*5)
                for i in range(1,37):
                    if i == 31 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen32(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_32.size().width() == 240:
                self.parent.ui.cmraBt_32.resize(1491 , 891)
                self.parent.ui.cmraBt_32.move(10,10)
                for i in range(1,37):
                    if i == 32 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_32.resize(240 , 138)
                self.parent.ui.cmraBt_32.move(10+240*1,10+140*5)
                for i in range(1,37):
                    if i == 32 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen33(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_33.size().width() == 240:
                self.parent.ui.cmraBt_33.resize(1491 , 891)
                self.parent.ui.cmraBt_33.move(10,10)
                for i in range(1,37):
                    if i == 33 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_33.resize(240 , 138)
                self.parent.ui.cmraBt_33.move(10+240*2,10+140*5)
                for i in range(1,37):
                    if i == 33 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen34(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_34.size().width() == 240:
                self.parent.ui.cmraBt_34.resize(1491 , 891)
                self.parent.ui.cmraBt_34.move(10,10)
                for i in range(1,37):
                    if i == 34 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_34.resize(240 , 138)
                self.parent.ui.cmraBt_34.move(10+240*3,10+140*5)
                for i in range(1,37):
                    if i == 34 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen35(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_35.size().width() == 240:
                self.parent.ui.cmraBt_35.resize(1491 , 891)
                self.parent.ui.cmraBt_35.move(10,10)
                for i in range(1,37):
                    if i == 35 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_35.resize(240 , 138)
                self.parent.ui.cmraBt_35.move(10+240*4,10+140*5)
                for i in range(1,37):
                    if i == 35 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
    def fullscreen36(self):
        now = time.time()
        if now - self.parent.dclickTime[1]  < 0.3:
            if self.parent.ui.cmraBt_36.size().width() == 240:
                self.parent.ui.cmraBt_36.resize(1491 , 891)
                self.parent.ui.cmraBt_36.move(10,10)
                for i in range(1,37):
                    if i == 36 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.hide()'%i)
            else:
                self.parent.ui.cmraBt_36.resize(240 , 138)
                self.parent.ui.cmraBt_36.move(10+240*5,10+140*5)
                for i in range(1,37):
                    if i == 36 :
                        pass
                    else :
                        exec('self.parent.ui.cmraBt_%02d.show()'%i)
        self.parent.dclickTime[1] = time.time()
    
