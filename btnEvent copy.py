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



class DragBtn(QPushButton):
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(self.text())
        drag.setMimeData(mimedata)
        pixmap = QPixmap(self.size())
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
        drag.exec_(Qt.CopyAction | Qt.MoveAction)

class DropBtn(QPushButton):
    def __init__(self, *args, **kwargs):
        QPushButton.__init__(self, *args, **kwargs)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        pos = event.pos()
        text = event.mimeData().text()
        self.setText(text)
        event.acceptProposedAction()

class btns():
    def __init__(self , ui):
        self.ui = ui

        self.ui.camVideo_01 = DropBtn(self.ui.ca_widget_01)
        self.ui.camVideo_01.resize(224,122)
        self.ui.camVideo_01.move(9,8)
        self.ui.camVideo_01.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_02 = DropBtn(self.ui.ca_widget_02)
        self.ui.camVideo_02.resize(224,122)
        self.ui.camVideo_02.move(9,8)
        self.ui.camVideo_02.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_03 = DropBtn(self.ui.ca_widget_03)
        self.ui.camVideo_03.resize(224,122)
        self.ui.camVideo_03.move(9,8)
        self.ui.camVideo_03.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_04 = DropBtn(self.ui.ca_widget_04)
        self.ui.camVideo_04.resize(224,122)
        self.ui.camVideo_04.move(9,8)
        self.ui.camVideo_04.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_05 = DropBtn(self.ui.ca_widget_05)
        self.ui.camVideo_05.resize(224,122)
        self.ui.camVideo_05.move(9,8)
        self.ui.camVideo_05.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_06 = DropBtn(self.ui.ca_widget_06)
        self.ui.camVideo_06.resize(224,122)
        self.ui.camVideo_06.move(9,8)
        self.ui.camVideo_06.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_07 = DropBtn(self.ui.ca_widget_07)
        self.ui.camVideo_07.resize(224,122)
        self.ui.camVideo_07.move(9,8)
        self.ui.camVideo_07.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_08 = DropBtn(self.ui.ca_widget_08)
        self.ui.camVideo_08.resize(224,122)
        self.ui.camVideo_08.move(9,8)
        self.ui.camVideo_08.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_09 = DropBtn(self.ui.ca_widget_09)
        self.ui.camVideo_09.resize(224,122)
        self.ui.camVideo_09.move(9,8)
        self.ui.camVideo_09.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_10 = DropBtn(self.ui.ca_widget_10)
        self.ui.camVideo_10.resize(224,122)
        self.ui.camVideo_10.move(9,8)
        self.ui.camVideo_10.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_11 = DropBtn(self.ui.ca_widget_11)
        self.ui.camVideo_11.resize(224,122)
        self.ui.camVideo_11.move(9,8)
        self.ui.camVideo_11.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_12 = DropBtn(self.ui.ca_widget_12)
        self.ui.camVideo_12.resize(224,122)
        self.ui.camVideo_12.move(9,8)
        self.ui.camVideo_12.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_13 = DropBtn(self.ui.ca_widget_13)
        self.ui.camVideo_13.resize(224,122)
        self.ui.camVideo_13.move(9,8)
        self.ui.camVideo_13.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_14 = DropBtn(self.ui.ca_widget_14)
        self.ui.camVideo_14.resize(224,122)
        self.ui.camVideo_14.move(9,8)
        self.ui.camVideo_14.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_15 = DropBtn(self.ui.ca_widget_15)
        self.ui.camVideo_15.resize(224,122)
        self.ui.camVideo_15.move(9,8)
        self.ui.camVideo_15.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_16 = DropBtn(self.ui.ca_widget_16)
        self.ui.camVideo_16.resize(224,122)
        self.ui.camVideo_16.move(9,8)
        self.ui.camVideo_16.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_17 = DropBtn(self.ui.ca_widget_17)
        self.ui.camVideo_17.resize(224,122)
        self.ui.camVideo_17.move(9,8)
        self.ui.camVideo_17.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_18 = DropBtn(self.ui.ca_widget_18)
        self.ui.camVideo_18.resize(224,122)
        self.ui.camVideo_18.move(9,8)
        self.ui.camVideo_18.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_19 = DropBtn(self.ui.ca_widget_19)
        self.ui.camVideo_19.resize(224,122)
        self.ui.camVideo_19.move(9,8)
        self.ui.camVideo_19.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_20 = DropBtn(self.ui.ca_widget_20)
        self.ui.camVideo_20.resize(224,122)
        self.ui.camVideo_20.move(9,8)
        self.ui.camVideo_20.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_21 = DropBtn(self.ui.ca_widget_21)
        self.ui.camVideo_21.resize(224,122)
        self.ui.camVideo_21.move(9,8)
        self.ui.camVideo_21.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_22 = DropBtn(self.ui.ca_widget_22)
        self.ui.camVideo_22.resize(224,122)
        self.ui.camVideo_22.move(9,8)
        self.ui.camVideo_22.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_23 = DropBtn(self.ui.ca_widget_23)
        self.ui.camVideo_23.resize(224,122)
        self.ui.camVideo_23.move(9,8)
        self.ui.camVideo_23.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_24 = DropBtn(self.ui.ca_widget_24)
        self.ui.camVideo_24.resize(224,122)
        self.ui.camVideo_24.move(9,8)
        self.ui.camVideo_24.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_25 = DropBtn(self.ui.ca_widget_25)
        self.ui.camVideo_25.resize(224,122)
        self.ui.camVideo_25.move(9,8)
        self.ui.camVideo_25.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_26 = DropBtn(self.ui.ca_widget_26)
        self.ui.camVideo_26.resize(224,122)
        self.ui.camVideo_26.move(9,8)
        self.ui.camVideo_26.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_27 = DropBtn(self.ui.ca_widget_27)
        self.ui.camVideo_27.resize(224,122)
        self.ui.camVideo_27.move(9,8)
        self.ui.camVideo_27.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_28 = DropBtn(self.ui.ca_widget_28)
        self.ui.camVideo_28.resize(224,122)
        self.ui.camVideo_28.move(9,8)
        self.ui.camVideo_28.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_29 = DropBtn(self.ui.ca_widget_29)
        self.ui.camVideo_29.resize(224,122)
        self.ui.camVideo_29.move(9,8)
        self.ui.camVideo_29.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_30 = DropBtn(self.ui.ca_widget_30)
        self.ui.camVideo_30.resize(224,122)
        self.ui.camVideo_30.move(9,8)
        self.ui.camVideo_30.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_31 = DropBtn(self.ui.ca_widget_31)
        self.ui.camVideo_31.resize(224,122)
        self.ui.camVideo_31.move(9,8)
        self.ui.camVideo_31.setStyleSheet("background-color: rgba(255, 255, 255, 3);")
        self.ui.camVideo_32 = DropBtn(self.ui.ca_widget_32)
        self.ui.camVideo_32.resize(224,122)
        self.ui.camVideo_32.move(9,8)
        self.ui.camVideo_32.setStyleSheet("background-color: rgba(255, 255, 255, 3);")

###asdasd###
        
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

        self.ui.camVideo_01.clicked.connect(self.fullscreen01)
        self.ui.camVideo_02.clicked.connect(self.fullscreen02)
        self.ui.camVideo_03.clicked.connect(self.fullscreen03)
        self.ui.camVideo_04.clicked.connect(self.fullscreen04)
        self.ui.camVideo_05.clicked.connect(self.fullscreen05)
        self.ui.camVideo_06.clicked.connect(self.fullscreen06)
        self.ui.camVideo_07.clicked.connect(self.fullscreen07)
        self.ui.camVideo_08.clicked.connect(self.fullscreen08)
        self.ui.camVideo_09.clicked.connect(self.fullscreen09)
        self.ui.camVideo_10.clicked.connect(self.fullscreen10)
        self.ui.camVideo_11.clicked.connect(self.fullscreen11)
        self.ui.camVideo_12.clicked.connect(self.fullscreen12)
        self.ui.camVideo_13.clicked.connect(self.fullscreen13)
        self.ui.camVideo_14.clicked.connect(self.fullscreen14)
        self.ui.camVideo_15.clicked.connect(self.fullscreen15)
        self.ui.camVideo_16.clicked.connect(self.fullscreen16)
        self.ui.camVideo_17.clicked.connect(self.fullscreen17)
        self.ui.camVideo_18.clicked.connect(self.fullscreen18)
        self.ui.camVideo_19.clicked.connect(self.fullscreen19)
        self.ui.camVideo_20.clicked.connect(self.fullscreen20)
        self.ui.camVideo_21.clicked.connect(self.fullscreen21)
        self.ui.camVideo_22.clicked.connect(self.fullscreen22)
        self.ui.camVideo_23.clicked.connect(self.fullscreen23)
        self.ui.camVideo_24.clicked.connect(self.fullscreen24)
        self.ui.camVideo_25.clicked.connect(self.fullscreen25)
        self.ui.camVideo_26.clicked.connect(self.fullscreen26)
        self.ui.camVideo_27.clicked.connect(self.fullscreen27)
        self.ui.camVideo_28.clicked.connect(self.fullscreen28)
        self.ui.camVideo_29.clicked.connect(self.fullscreen29)
        self.ui.camVideo_30.clicked.connect(self.fullscreen30)
        self.ui.camVideo_31.clicked.connect(self.fullscreen31)
        self.ui.camVideo_32.clicked.connect(self.fullscreen32)
        self.cameras = {"cam01" : self.ui.camVideo_01, "cam02" : self.ui.camVideo_02, "cam03" : self.ui.camVideo_03, 
                        "cam04" : self.ui.camVideo_04, "cam05" : self.ui.camVideo_05, "cam06" : self.ui.camVideo_06, "cam07" : self.ui.camVideo_07, 
                        "cam08" : self.ui.camVideo_08, "cam09" : self.ui.camVideo_09, "cam10" : self.ui.camVideo_10, "cam11" : self.ui.camVideo_11, 
                        "cam12" : self.ui.camVideo_12, "cam13" : self.ui.camVideo_13, "cam14" : self.ui.camVideo_14, "cam15" : self.ui.camVideo_15, 
                        "cam16" : self.ui.camVideo_16, "cam17" : self.ui.camVideo_17, "cam18" : self.ui.camVideo_18, "cam19" : self.ui.camVideo_19, 
                        "cam20" : self.ui.camVideo_20, "cam21" : self.ui.camVideo_21, "cam22" : self.ui.camVideo_22, "cam23" : self.ui.camVideo_23, 
                        "cam24" : self.ui.camVideo_24, "cam25" : self.ui.camVideo_25, "cam26" : self.ui.camVideo_26, "cam27" : self.ui.camVideo_27, 
                        "cam28" : self.ui.camVideo_28, "cam29" : self.ui.camVideo_29, "cam30" : self.ui.camVideo_30, "cam31" : self.ui.camVideo_31, 
                        "cam32" : self.ui.camVideo_32}

        for cam in self.cameras:
            self.cameras[cam].full = False
            self.cameras[cam].active = True

        self.fullscreens = [self.showall ,self.showLayer1 ,self.showLayer2 ]
        self.layers = {
            "6":[self.ui.camVideo_01,
            self.ui.camVideo_03,
            self.ui.camVideo_09,
            self.ui.camVideo_13,
            self.ui.camVideo_14,
            self.ui.camVideo_15
            ],
            "7_1":
            [self.ui.camVideo_01,
            self.ui.camVideo_04,
            self.ui.camVideo_10,
            self.ui.camVideo_16,
            self.ui.camVideo_19,
            self.ui.camVideo_20,
            self.ui.camVideo_21,
            self.ui.camVideo_22
            ],
            "7_2":
            [self.ui.camVideo_01,
            self.ui.camVideo_03,
            self.ui.camVideo_13,
            self.ui.camVideo_14,
            self.ui.camVideo_15,
            self.ui.camVideo_19,
            self.ui.camVideo_20
            ],
            "10":
            [self.ui.camVideo_01,
            self.ui.camVideo_03,
            self.ui.camVideo_13,
            self.ui.camVideo_14,
            self.ui.camVideo_15,
            self.ui.camVideo_16,
            self.ui.camVideo_19,
            self.ui.camVideo_20,
            self.ui.camVideo_21,
            self.ui.camVideo_22,
            ],
            "13":
            [self.ui.camVideo_01,
            self.ui.camVideo_03,
            self.ui.camVideo_04,
            self.ui.camVideo_07,
            self.ui.camVideo_08,
            self.ui.camVideo_13,
            self.ui.camVideo_14,
            self.ui.camVideo_15,
            self.ui.camVideo_16,
            self.ui.camVideo_19,
            self.ui.camVideo_20,
            self.ui.camVideo_21,
            self.ui.camVideo_22,
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
        """listwidget = self.ui.cmr_listWidget
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
            item.setBackground( QColor(0,200,0) )"""

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


