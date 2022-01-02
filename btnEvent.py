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
import pickle
import json


class DragBtn(QPushButton):
    def __init__(self, *args, **kwargs):
        QPushButton.__init__(self, *args, **kwargs)
        self.clickTime = time.time()
        self.setData = {}

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()
        if time.time()  - self.clickTime < 0.3:
            self.func(base=True)
        self.clickTime = time.time()
        self.parent.baseCamNum = int(self.idx)-1
        print("self.idx" , self.idx)

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(json.dumps(self.parent.camBaseSettings[self.parent.baseCamNum]))
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

        print("self.parent.baseCamNum2" ,self.parent.baseCamNum)
        self.parent.camSettings[self.parent.currentLayer][self.num]["ip"] = self.parent.camBaseSettings[self.parent.baseCamNum]["ip"]
        name = self.parent.camSettings[self.parent.currentLayer][self.num]["name"] = self.parent.camBaseSettings[self.parent.baseCamNum]["name"]
        loc = self.parent.camSettings[self.parent.currentLayer][self.num]["location"] = self.parent.camBaseSettings[self.parent.baseCamNum]["location"]
        print("name" , name , "loc" , loc)
        self.parent.camSettings[self.parent.currentLayer][self.num]["zoom"] = self.parent.camBaseSettings[self.parent.baseCamNum]["zoom"]
        self.parent.camSettings[self.parent.currentLayer][self.num]["sens"] = self.parent.camBaseSettings[self.parent.baseCamNum]["sens"]
        self.parent.camSettings[self.parent.currentLayer][self.num]["focus"] = self.parent.camBaseSettings[self.parent.baseCamNum]["focus"]
        self.parent.camSettings[self.parent.currentLayer][self.num]["memo"] = self.parent.camBaseSettings[self.parent.baseCamNum]["memo"]
        self.parent.settings['camsetting'] = self.parent.camSettings
        with open(self.parent.setFileName, "wb") as f:
            pickle.dump(self.parent.settings , f)
        self.parent.currentCam = self.num

        self.parent.loadCameraSet()
        pos = event.pos()
        text = event.mimeData().text()
        #print(dir(event.mimeData()))
        if loc.strip():
            self.setText(loc)
        else:
            self.setText(name)
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

        for bidx in range(1 , 33):
            exec(f'''self.ui.camVideo_{bidx:02d}.parent = self''')
            exec(f'''self.ui.camVideo_{bidx:02d}.num = "cam{bidx:02d}"''')
            exec(f'''self.ui.camVideo_{bidx:02d}.alarm = QLabel(self.ui.ca_widget_{bidx:02d})''')
            exec(f'''self.ui.camVideo_{bidx:02d}.alarm.move(0,0)''')
            exec(f'''self.ui.camVideo_{bidx:02d}.alarm.resize(240,21)''')
            exec(f'''self.ui.camVideo_{bidx:02d}.alarm.setStyleSheet("background-color: rgba(255, 255, 255, 50);")''')



        self.ui.cmraBt_01 = DragBtn(self.ui.dragCamBase )
        self.ui.cmraBt_01.func = self.showSetting
        self.ui.cmraBt_01.resize(51,30)
        self.ui.cmraBt_01.parent = self
        self.ui.cmraBt_01.move(int(20+50*0), int(60 + 40*0) )
        self.ui.cmraBt_01.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_01.setIconSize(QSize(28,28))
        self.ui.cmraBt_01.setText("01")
        self.ui.cmraBt_01.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_01.idx=self.ui.cmraBt_01.text()
        self.ui.cmraBt_02 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_02.func = self.showSetting
        self.ui.cmraBt_02.resize(51,30)
        self.ui.cmraBt_02.parent = self
        self.ui.cmraBt_02.move(int(20+50*1), int(60 + 40*0) )
        self.ui.cmraBt_02.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_02.setIconSize(QSize(28,28))
        self.ui.cmraBt_02.setText("02")
        self.ui.cmraBt_02.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_02.idx=self.ui.cmraBt_02.text()
        self.ui.cmraBt_03 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_03.func = self.showSetting
        self.ui.cmraBt_03.resize(51,30)
        self.ui.cmraBt_03.parent = self
        self.ui.cmraBt_03.move(int(20+50*2), int(60 + 40*0) )
        self.ui.cmraBt_03.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_03.setIconSize(QSize(28,28))
        self.ui.cmraBt_03.setText("03")
        self.ui.cmraBt_03.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_03.idx=self.ui.cmraBt_03.text()
        self.ui.cmraBt_04 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_04.func = self.showSetting
        self.ui.cmraBt_04.resize(51,30)
        self.ui.cmraBt_04.parent = self
        self.ui.cmraBt_04.move(int(20+50*3), int(60 + 40*0) )
        self.ui.cmraBt_04.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_04.setIconSize(QSize(28,28))
        self.ui.cmraBt_04.setText("04")
        self.ui.cmraBt_04.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_04.idx=self.ui.cmraBt_04.text()
        self.ui.cmraBt_05 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_05.func = self.showSetting
        self.ui.cmraBt_05.resize(51,30)
        self.ui.cmraBt_05.parent = self
        self.ui.cmraBt_05.move(int(20+50*4), int(60 + 40*0) )
        self.ui.cmraBt_05.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_05.setIconSize(QSize(28,28))
        self.ui.cmraBt_05.setText("05")
        self.ui.cmraBt_05.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_05.idx=self.ui.cmraBt_05.text()
        self.ui.cmraBt_06 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_06.func = self.showSetting
        self.ui.cmraBt_06.resize(51,30)
        self.ui.cmraBt_06.parent = self
        self.ui.cmraBt_06.move(int(20+50*5), int(60 + 40*0) )
        self.ui.cmraBt_06.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_06.setIconSize(QSize(28,28))
        self.ui.cmraBt_06.setText("06")
        self.ui.cmraBt_06.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_06.idx=self.ui.cmraBt_06.text()
        self.ui.cmraBt_07 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_07.func = self.showSetting
        self.ui.cmraBt_07.resize(51,30)
        self.ui.cmraBt_07.parent = self
        self.ui.cmraBt_07.move(int(20+50*0), int(60 + 40*1) )
        self.ui.cmraBt_07.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_07.setIconSize(QSize(28,28))
        self.ui.cmraBt_07.setText("07")
        self.ui.cmraBt_07.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_07.idx=self.ui.cmraBt_07.text()
        self.ui.cmraBt_08 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_08.func = self.showSetting
        self.ui.cmraBt_08.resize(51,30)
        self.ui.cmraBt_08.parent = self
        self.ui.cmraBt_08.move(int(20+50*1), int(60 + 40*1) )
        self.ui.cmraBt_08.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_08.setIconSize(QSize(28,28))
        self.ui.cmraBt_08.setText("08")
        self.ui.cmraBt_08.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_08.idx=self.ui.cmraBt_08.text()
        self.ui.cmraBt_09 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_09.func = self.showSetting
        self.ui.cmraBt_09.resize(51,30)
        self.ui.cmraBt_09.parent = self
        self.ui.cmraBt_09.move(int(20+50*2), int(60 + 40*1) )
        self.ui.cmraBt_09.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_09.setIconSize(QSize(28,28))
        self.ui.cmraBt_09.setText("09")
        self.ui.cmraBt_09.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_09.idx=self.ui.cmraBt_09.text()
        self.ui.cmraBt_10 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_10.func = self.showSetting
        self.ui.cmraBt_10.resize(51,30)
        self.ui.cmraBt_10.parent = self
        self.ui.cmraBt_10.move(int(20+50*3), int(60 + 40*1) )
        self.ui.cmraBt_10.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_10.setIconSize(QSize(28,28))
        self.ui.cmraBt_10.setText("10")
        self.ui.cmraBt_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_10.idx=self.ui.cmraBt_10.text()
        self.ui.cmraBt_11 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_11.func = self.showSetting
        self.ui.cmraBt_11.resize(51,30)
        self.ui.cmraBt_11.parent = self
        self.ui.cmraBt_11.move(int(20+50*4), int(60 + 40*1) )
        self.ui.cmraBt_11.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_11.setIconSize(QSize(28,28))
        self.ui.cmraBt_11.setText("11")
        self.ui.cmraBt_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_11.idx=self.ui.cmraBt_11.text()
        self.ui.cmraBt_12 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_12.func = self.showSetting
        self.ui.cmraBt_12.resize(51,30)
        self.ui.cmraBt_12.parent = self
        self.ui.cmraBt_12.move(int(20+50*5), int(60 + 40*1) )
        self.ui.cmraBt_12.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_12.setIconSize(QSize(28,28))
        self.ui.cmraBt_12.setText("12")
        self.ui.cmraBt_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_12.idx=self.ui.cmraBt_12.text()
        self.ui.cmraBt_13 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_13.func = self.showSetting
        self.ui.cmraBt_13.resize(51,30)
        self.ui.cmraBt_13.parent = self
        self.ui.cmraBt_13.move(int(20+50*0), int(60 + 40*2) )
        self.ui.cmraBt_13.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_13.setIconSize(QSize(28,28))
        self.ui.cmraBt_13.setText("13")
        self.ui.cmraBt_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_13.idx=self.ui.cmraBt_13.text()
        self.ui.cmraBt_14 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_14.func = self.showSetting
        self.ui.cmraBt_14.resize(51,30)
        self.ui.cmraBt_14.parent = self
        self.ui.cmraBt_14.move(int(20+50*1), int(60 + 40*2) )
        self.ui.cmraBt_14.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_14.setIconSize(QSize(28,28))
        self.ui.cmraBt_14.setText("14")
        self.ui.cmraBt_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_14.idx=self.ui.cmraBt_14.text()
        self.ui.cmraBt_15 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_15.func = self.showSetting
        self.ui.cmraBt_15.resize(51,30)
        self.ui.cmraBt_15.parent = self
        self.ui.cmraBt_15.move(int(20+50*2), int(60 + 40*2) )
        self.ui.cmraBt_15.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_15.setIconSize(QSize(28,28))
        self.ui.cmraBt_15.setText("15")
        self.ui.cmraBt_15.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_15.idx=self.ui.cmraBt_15.text()
        self.ui.cmraBt_16 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_16.func = self.showSetting
        self.ui.cmraBt_16.resize(51,30)
        self.ui.cmraBt_16.parent = self
        self.ui.cmraBt_16.move(int(20+50*3), int(60 + 40*2) )
        self.ui.cmraBt_16.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_16.setIconSize(QSize(28,28))
        self.ui.cmraBt_16.setText("16")
        self.ui.cmraBt_16.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_16.idx=self.ui.cmraBt_16.text()
        self.ui.cmraBt_17 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_17.func = self.showSetting
        self.ui.cmraBt_17.resize(51,30)
        self.ui.cmraBt_17.parent = self
        self.ui.cmraBt_17.move(int(20+50*4), int(60 + 40*2) )
        self.ui.cmraBt_17.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_17.setIconSize(QSize(28,28))
        self.ui.cmraBt_17.setText("17")
        self.ui.cmraBt_17.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_17.idx=self.ui.cmraBt_17.text()
        self.ui.cmraBt_18 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_18.func = self.showSetting
        self.ui.cmraBt_18.resize(51,30)
        self.ui.cmraBt_18.parent = self
        self.ui.cmraBt_18.move(int(20+50*5), int(60 + 40*2) )
        self.ui.cmraBt_18.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_18.setIconSize(QSize(28,28))
        self.ui.cmraBt_18.setText("18")
        self.ui.cmraBt_18.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_18.idx=self.ui.cmraBt_18.text()
        self.ui.cmraBt_19 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_19.func = self.showSetting
        self.ui.cmraBt_19.resize(51,30)
        self.ui.cmraBt_19.parent = self
        self.ui.cmraBt_19.move(int(20+50*0), int(60 + 40*3) )
        self.ui.cmraBt_19.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_19.setIconSize(QSize(28,28))
        self.ui.cmraBt_19.setText("19")
        self.ui.cmraBt_19.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_19.idx=self.ui.cmraBt_19.text()
        self.ui.cmraBt_20 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_20.func = self.showSetting
        self.ui.cmraBt_20.resize(51,30)
        self.ui.cmraBt_20.parent = self
        self.ui.cmraBt_20.move(int(20+50*1), int(60 + 40*3) )
        self.ui.cmraBt_20.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_20.setIconSize(QSize(28,28))
        self.ui.cmraBt_20.setText("20")
        self.ui.cmraBt_20.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_20.idx=self.ui.cmraBt_20.text()
        self.ui.cmraBt_21 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_21.func = self.showSetting
        self.ui.cmraBt_21.resize(51,30)
        self.ui.cmraBt_21.parent = self
        self.ui.cmraBt_21.move(int(20+50*2), int(60 + 40*3) )
        self.ui.cmraBt_21.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_21.setIconSize(QSize(28,28))
        self.ui.cmraBt_21.setText("21")
        self.ui.cmraBt_21.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_21.idx=self.ui.cmraBt_21.text()
        self.ui.cmraBt_22 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_22.func = self.showSetting
        self.ui.cmraBt_22.resize(51,30)
        self.ui.cmraBt_22.parent = self
        self.ui.cmraBt_22.move(int(20+50*3), int(60 + 40*3) )
        self.ui.cmraBt_22.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_22.setIconSize(QSize(28,28))
        self.ui.cmraBt_22.setText("22")
        self.ui.cmraBt_22.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_22.idx=self.ui.cmraBt_22.text()
        self.ui.cmraBt_23 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_23.func = self.showSetting
        self.ui.cmraBt_23.resize(51,30)
        self.ui.cmraBt_23.parent = self
        self.ui.cmraBt_23.move(int(20+50*4), int(60 + 40*3) )
        self.ui.cmraBt_23.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_23.setIconSize(QSize(28,28))
        self.ui.cmraBt_23.setText("23")
        self.ui.cmraBt_23.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_23.idx=self.ui.cmraBt_23.text()
        self.ui.cmraBt_24 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_24.func = self.showSetting
        self.ui.cmraBt_24.resize(51,30)
        self.ui.cmraBt_24.parent = self
        self.ui.cmraBt_24.move(int(20+50*5), int(60 + 40*3) )
        self.ui.cmraBt_24.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_24.setIconSize(QSize(28,28))
        self.ui.cmraBt_24.setText("24")
        self.ui.cmraBt_24.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_24.idx=self.ui.cmraBt_24.text()
        self.ui.cmraBt_25 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_25.func = self.showSetting
        self.ui.cmraBt_25.resize(51,30)
        self.ui.cmraBt_25.parent = self
        self.ui.cmraBt_25.move(int(20+50*0), int(60 + 40*4) )
        self.ui.cmraBt_25.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_25.setIconSize(QSize(28,28))
        self.ui.cmraBt_25.setText("25")
        self.ui.cmraBt_25.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_25.idx=self.ui.cmraBt_25.text()
        self.ui.cmraBt_26 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_26.func = self.showSetting
        self.ui.cmraBt_26.resize(51,30)
        self.ui.cmraBt_26.parent = self
        self.ui.cmraBt_26.move(int(20+50*1), int(60 + 40*4) )
        self.ui.cmraBt_26.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_26.setIconSize(QSize(28,28))
        self.ui.cmraBt_26.setText("26")
        self.ui.cmraBt_26.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_26.idx=self.ui.cmraBt_26.text()
        self.ui.cmraBt_27 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_27.func = self.showSetting
        self.ui.cmraBt_27.resize(51,30)
        self.ui.cmraBt_27.parent = self
        self.ui.cmraBt_27.move(int(20+50*2), int(60 + 40*4) )
        self.ui.cmraBt_27.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_27.setIconSize(QSize(28,28))
        self.ui.cmraBt_27.setText("27")
        self.ui.cmraBt_27.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_27.idx=self.ui.cmraBt_27.text()
        self.ui.cmraBt_28 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_28.func = self.showSetting
        self.ui.cmraBt_28.resize(51,30)
        self.ui.cmraBt_28.parent = self
        self.ui.cmraBt_28.move(int(20+50*3), int(60 + 40*4) )
        self.ui.cmraBt_28.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_28.setIconSize(QSize(28,28))
        self.ui.cmraBt_28.setText("28")
        self.ui.cmraBt_28.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_28.idx=self.ui.cmraBt_28.text()
        self.ui.cmraBt_29 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_29.func = self.showSetting
        self.ui.cmraBt_29.resize(51,30)
        self.ui.cmraBt_29.parent = self
        self.ui.cmraBt_29.move(int(20+50*4), int(60 + 40*4) )
        self.ui.cmraBt_29.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_29.setIconSize(QSize(28,28))
        self.ui.cmraBt_29.setText("29")
        self.ui.cmraBt_29.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_29.idx=self.ui.cmraBt_29.text()
        self.ui.cmraBt_30 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_30.func = self.showSetting
        self.ui.cmraBt_30.resize(51,30)
        self.ui.cmraBt_30.parent = self
        self.ui.cmraBt_30.move(int(20+50*5), int(60 + 40*4) )
        self.ui.cmraBt_30.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_30.setIconSize(QSize(28,28))
        self.ui.cmraBt_30.setText("30")
        self.ui.cmraBt_30.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_30.idx=self.ui.cmraBt_30.text()
        self.ui.cmraBt_31 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_31.func = self.showSetting
        self.ui.cmraBt_31.resize(51,30)
        self.ui.cmraBt_31.parent = self
        self.ui.cmraBt_31.move(int(20+50*0), int(60 + 40*5) )
        self.ui.cmraBt_31.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_31.setIconSize(QSize(28,28))
        self.ui.cmraBt_31.setText("31")
        self.ui.cmraBt_31.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_31.idx=self.ui.cmraBt_31.text()
        self.ui.cmraBt_32 = DragBtn(self.ui.dragCamBase)
        self.ui.cmraBt_32.func = self.showSetting
        self.ui.cmraBt_32.resize(51,30)
        self.ui.cmraBt_32.parent = self
        self.ui.cmraBt_32.move(int(20+50*1), int(60 + 40*5) )
        self.ui.cmraBt_32.setIcon(QPixmap(u"datas/images/bt1.png"))
        self.ui.cmraBt_32.setIconSize(QSize(28,28))
        self.ui.cmraBt_32.setText("32")
        self.ui.cmraBt_32.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.cmraBt_32.idx=self.ui.cmraBt_32.text()
        
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
    
        self.camDropLabels = {"cam01" : self.ui.ca_label_01, "cam02" : self.ui.ca_label_02, "cam03" : self.ui.ca_label_03, 
                        "cam04" : self.ui.ca_label_04, "cam05" : self.ui.ca_label_05, "cam06" : self.ui.ca_label_06, "cam07" : self.ui.ca_label_07, 
                        "cam08" : self.ui.ca_label_08, "cam09" : self.ui.ca_label_09, "cam10" : self.ui.ca_label_10, "cam11" : self.ui.ca_label_11, 
                        "cam12" : self.ui.ca_label_12, "cam13" : self.ui.ca_label_13, "cam14" : self.ui.ca_label_14, "cam15" : self.ui.ca_label_15, 
                        "cam16" : self.ui.ca_label_16, "cam17" : self.ui.ca_label_17, "cam18" : self.ui.ca_label_18, "cam19" : self.ui.ca_label_19, 
                        "cam20" : self.ui.ca_label_20, "cam21" : self.ui.ca_label_21, "cam22" : self.ui.ca_label_22, "cam23" : self.ui.ca_label_23, 
                        "cam24" : self.ui.ca_label_24, "cam25" : self.ui.ca_label_25, "cam26" : self.ui.ca_label_26, "cam27" : self.ui.ca_label_27, 
                        "cam28" : self.ui.ca_label_28, "cam29" : self.ui.ca_label_29, "cam30" : self.ui.ca_label_30, "cam31" : self.ui.ca_label_31, 
                        "cam32" : self.ui.ca_label_32}

        self.camDropWidgets = {"cam01" : self.ui.ca_widget_01, "cam02" : self.ui.ca_widget_02, "cam03" : self.ui.ca_widget_03, 
                        "cam04" : self.ui.ca_widget_04, "cam05" : self.ui.ca_widget_05, "cam06" : self.ui.ca_widget_06, "cam07" : self.ui.ca_widget_07, 
                        "cam08" : self.ui.ca_widget_08, "cam09" : self.ui.ca_widget_09, "cam10" : self.ui.ca_widget_10, "cam11" : self.ui.ca_widget_11, 
                        "cam12" : self.ui.ca_widget_12, "cam13" : self.ui.ca_widget_13, "cam14" : self.ui.ca_widget_14, "cam15" : self.ui.ca_widget_15, 
                        "cam16" : self.ui.ca_widget_16, "cam17" : self.ui.ca_widget_17, "cam18" : self.ui.ca_widget_18, "cam19" : self.ui.ca_widget_19, 
                        "cam20" : self.ui.ca_widget_20, "cam21" : self.ui.ca_widget_21, "cam22" : self.ui.ca_widget_22, "cam23" : self.ui.ca_widget_23, 
                        "cam24" : self.ui.ca_widget_24, "cam25" : self.ui.ca_widget_25, "cam26" : self.ui.ca_widget_26, "cam27" : self.ui.ca_widget_27, 
                        "cam28" : self.ui.ca_widget_28, "cam29" : self.ui.ca_widget_29, "cam30" : self.ui.ca_widget_30, "cam31" : self.ui.ca_widget_31, 
                        "cam32" : self.ui.ca_widget_32}


        self.camDragBtns = {"cam01" : self.ui.cmraBt_01, "cam02" : self.ui.cmraBt_02, "cam03" : self.ui.cmraBt_03, 
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

        self.fullscreens = [self.showall ,self.showLayer1 ,self.showLayer2 ,self.showLayer3,self.showLayer4,self.showLayer5]
        self.layers = {
            "6":['cam01','cam03','cam09','cam13','cam14','cam15'],

            "7_1":
            ['cam01',
            'cam04',
            'cam10',
            'cam16',
            'cam19',
            'cam20',
            'cam21',
            'cam22'
            ],
            "7_2":
            ['cam01',
            'cam03',
            'cam13',
            'cam14',
            'cam15',
            'cam19',
            'cam20'
            ],
            "10":
            ['cam01',
            'cam03',
            'cam13',
            'cam14',
            'cam15',
            'cam16',
            'cam19',
            'cam20',
            'cam21',
            'cam22',
            ],
            "13":
            ['cam01',
            'cam03',
            'cam04',
            'cam07',
            'cam08',
            'cam13',
            'cam14',
            'cam15',
            'cam16',
            'cam19',
            'cam20',
            'cam21',
            'cam22',
            ],

        }
 


    def showSetting(self , base = False):
        if base and self.inFullScreenMode:
            self.resizeCamers(self.currentCam   , self.camDropWidgets)

        if self.settingLayer.isHidden():
            if base:
                self.inBaseSet = True
            else:
                self.inBaseSet = False
            self.loadCameraSet(base = base)
            self.settingLayer.show()
            self.settingLayer.resize(259 , 831)
            self.settingLayer.move(500-76 , 80-10)
            self.settingLayer.setStyleSheet('background-color: rgba(0, 52, 63, 255);')

        else:
            if base:
                self.inBaseSet = True
            else:
                self.inBaseSet = False
            self.settingLayer.hide()
            self.settingLayer.resize(259 , 831)
            self.settingLayer.move(1567 , 80)
            self.settingLayer.setStyleSheet(u"background-color: rgba(50, 50, 80, 50);")



#showSetting17
    def showall(self):
        self.currentLayer = 0
        self.setlistcolors()
        self.changelistColor()
        for cidx  , cam in enumerate(self.cameras):
            camera = self.cameras[cam]
            camera.active=True
            camera.show()
            camera.resize(231 , 131)
            self.camDropWidgets[cam].resize(231 , 131)
            self.camDropWidgets[cam].move( 10+231*(cidx%6) , 10+131*(cidx//6))
            self.camDropWidgets[cam].show()
            pixmap = QtGui.QPixmap("./datas/images/full0.png")
            pixmap.scaled(231, 131)
            self.camDropLabels[cam].resize(231 , 131)
            self.camDropLabels[cam].move(0,0)
            self.camDropLabels[cam].setPixmap(pixmap)
            camera.alarm.resize(231 , 21)


    def showLayer1(self):
        if self.allStoped==False:
            self.allStop(noask=True)
            self.allStart(noask=True)
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
            self.camDropWidgets[cam].hide()
            self.cameras[cam].active = False
        for cidx  , cam in enumerate(self.layers["6"]):
            camera = self.cameras[cam]
            camera.active=True
            camera.show()
            if cidx == 0:
                x = l[cidx][0]
                y = l[cidx][1]
                w = l[cidx][2] - l[cidx][0]
                h = l[cidx][3] - l[cidx][1]
                camera.resize(w,h)
                self.camDropWidgets[cam].resize(w , h)
                self.camDropWidgets[cam].move( x,y)#10+w*(cidx%6) , 10+h*(cidx//6))
                self.camDropWidgets[cam].show()
                pixmap = QtGui.QPixmap("./datas/images/full0.png")
                pixmap.scaled(231, 131)
                self.camDropLabels[cam].resize(w , h)
                self.camDropLabels[cam].move(0,0)
                self.camDropLabels[cam].setPixmap(pixmap)
                camera.alarm.resize(231 , 21)
            else:
                x = l[cidx][0]
                y = l[cidx][1]
                #camera.move(x+10,y+10)
                camera.resize(w0,h0)
                self.camDropWidgets[cam].resize(w0 , h0)
                self.camDropWidgets[cam].move( x,y)#10+w*(cidx%6) , 10+h*(cidx//6))
                self.camDropWidgets[cam].show()
                pixmap = QtGui.QPixmap("./datas/images/full0.png")
                pixmap.scaled(231, 131)
                self.camDropLabels[cam].resize(w0 , h0)
                self.camDropLabels[cam].move(0,0)
                self.camDropLabels[cam].setPixmap(pixmap)
                camera.alarm.resize(w0 , 21)


    def showLayer2(self):
        if self.allStoped==False:
            self.allStop(noask=True)
            self.allStart(noask=True)
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
            self.camDropWidgets[cam].hide()
            self.cameras[cam].active = False
        for cidx  , cam in enumerate(self.layers["7_1"]):
            camera = self.cameras[cam]
            camera.show()
            camera.active = True
            x = l[cidx][0]
            y = l[cidx][1]
            w = l[cidx][2] - l[cidx][0]
            h = l[cidx][3] - l[cidx][1]
            camera.resize(w,h)
            self.camDropWidgets[cam].resize(w , h)
            self.camDropWidgets[cam].move( x,y)#10+w*(cidx%6) , 10+h*(cidx//6))
            self.camDropWidgets[cam].show()
            pixmap = QtGui.QPixmap("./datas/images/full0.png")
            pixmap.scaled(231, 131)
            self.camDropLabels[cam].resize(w , h)
            self.camDropLabels[cam].move(0,0)
            self.camDropLabels[cam].setPixmap(pixmap)  
            camera.alarm.resize(w , 21) 

    def showLayer3(self):
        if self.allStoped==False:
            self.allStop(noask=True)
            self.allStart(noask=True)
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
            self.camDropWidgets[cam].hide()
            self.cameras[cam].active = False
        for cidx  , cam in enumerate(self.layers["7_2"]):
            camera = self.cameras[cam]
            camera.show()
            camera.active = True
            x = l[cidx][0]
            y = l[cidx][1]
            w = l[cidx][2] - l[cidx][0]
            h = l[cidx][3] - l[cidx][1]
            camera.resize(w,h)
            self.camDropWidgets[cam].resize(w , h)
            self.camDropWidgets[cam].move( x,y)#10+w*(cidx%6) , 10+h*(cidx//6))
            self.camDropWidgets[cam].show()
            pixmap = QtGui.QPixmap("./datas/images/full0.png")
            pixmap.scaled(231, 131)
            self.camDropLabels[cam].resize(w , h)
            self.camDropLabels[cam].move(0,0)
            self.camDropLabels[cam].setPixmap(pixmap)  
            camera.alarm.resize(w , 21)  

    def showLayer4(self):
        if self.allStoped==False:
            self.allStop(noask=True)
            self.allStart(noask=True)
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
            self.camDropWidgets[cam].hide()
            self.cameras[cam].active = False
        for cidx  , cam in enumerate(self.layers["10"]):
            camera = self.cameras[cam]
            camera.show()
            camera.active = True
            x = l[cidx][0]
            y = l[cidx][1]
            w = l[cidx][2] - l[cidx][0]
            h = l[cidx][3] - l[cidx][1]
            camera.resize(w,h)
            self.camDropWidgets[cam].resize(w , h)
            self.camDropWidgets[cam].move( x,y)#10+w*(cidx%6) , 10+h*(cidx//6))
            self.camDropWidgets[cam].show()
            pixmap = QtGui.QPixmap("./datas/images/full0.png")
            pixmap.scaled(231, 131)
            self.camDropLabels[cam].resize(w , h)
            self.camDropLabels[cam].move(0,0)
            self.camDropLabels[cam].setPixmap(pixmap)   
            camera.alarm.resize(w , 21) 

    def showLayer5(self):
        if self.allStoped==False:
            self.allStop(noask=True)
            self.allStart(noask=True)
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
            self.camDropWidgets[cam].hide()
            self.cameras[cam].active = False
        for cidx  , cam in enumerate(self.layers["13"]):
            camera = self.cameras[cam]
            camera.show()
            camera.active = True
            x = l[cidx][0]
            y = l[cidx][1]
            w = l[cidx][2] - l[cidx][0]
            h = l[cidx][3] - l[cidx][1]
            camera.resize(w,h)
            self.camDropWidgets[cam].resize(w , h)
            self.camDropWidgets[cam].move( x,y)#10+w*(cidx%6) , 10+h*(cidx//6))
            self.camDropWidgets[cam].show()
            pixmap = QtGui.QPixmap("./datas/images/full0.png")
            pixmap.scaled(231, 131)
            self.camDropLabels[cam].resize(w , h)
            self.camDropLabels[cam].move(0,0)
            self.camDropLabels[cam].setPixmap(pixmap) 
            camera.alarm.resize(w , 21)  

    def resizeCamers(self,cam , widgets):
        camera = self.cameras[cam]
        widget = widgets[cam]
        alarm = camera.alarm
        if camera.full:
            camera.full = False
            self.inFullScreenMode = False
            for cam_ in self.cameras:
                self.cameras[cam_].hide()
                widgets[cam_].hide()
                self.camDropLabels[cam].show()
            self.fullscreens[self.currentLayer]()
            self.settingLayer.hide()
        else:
            camera.full = True
            for cam_ in self.cameras:
                if cam != cam_:
                    self.cameras[cam_].hide()
                    widgets[cam_].hide()
            camera.resize(1411 , 831)
            alarm.resize(1411, 50)
            camera.move(0,0)
            camera.show()
            widget.resize(1411 , 831)
            widget.move(10,10)
            self.camDropLabels[cam].hide()
            widget.show()
            self.settingLayer.show()
            self.settingLayer.resize(259 , 831)
            self.settingLayer.move(1567 , 80)
            camera.alarm.resize(1411 , 21) 



    def fullscreen01(self):
        self.inBaseSet=False
        self.inBaseSet=False
        self.currentCam = 'cam01'
        self.loadCameraSet()        
        self.setLayerCorlr()
        now = time.time()
        if now - self.dclickTime[1]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[1] = time.time()




    def fullscreen02(self):
        self.inBaseSet=False
        self.currentCam = 'cam02'
        self.loadCameraSet()
        self.setLayerCorlr()
        now = time.time()
        if now - self.dclickTime[2]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[2] = time.time()

    def fullscreen03(self):
        self.inBaseSet=False
        self.currentCam = 'cam03'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[3]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[3] = time.time()

    def fullscreen04(self):
        self.inBaseSet=False
        self.currentCam = 'cam04'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[4]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[4] = time.time()

    def fullscreen05(self):
        self.inBaseSet=False
        self.currentCam = 'cam05'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[5]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[5] = time.time()

    def fullscreen06(self):
        self.inBaseSet=False
        self.currentCam = 'cam06'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[6]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[6] = time.time()

    def fullscreen07(self):
        self.inBaseSet=False
        self.currentCam = 'cam07'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[7]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[7] = time.time()

    def fullscreen08(self):
        self.inBaseSet=False
        self.currentCam = 'cam08'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[8]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[8] = time.time()

    def fullscreen09(self):
        self.inBaseSet=False
        self.currentCam = 'cam09'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[9]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[9] = time.time()

    def fullscreen10(self):
        self.inBaseSet=False
        self.currentCam = 'cam10'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[10]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[10] = time.time()

    def fullscreen11(self):
        self.inBaseSet=False
        self.currentCam = 'cam11'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[11]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[11] = time.time()

    def fullscreen12(self):
        self.inBaseSet=False
        self.currentCam = 'cam12'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[12]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[12] = time.time()

    def fullscreen13(self):
        self.inBaseSet=False
        self.currentCam = 'cam13'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[13]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[13] = time.time()

    def fullscreen14(self):
        self.inBaseSet=False
        self.currentCam = 'cam14'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[14]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[14] = time.time()

    def fullscreen15(self):
        self.inBaseSet=False
        self.currentCam = 'cam15'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[15]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[15] = time.time()

    def fullscreen16(self):
        self.inBaseSet=False
        self.currentCam = 'cam16'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[16]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[16] = time.time()

    def fullscreen17(self):
        self.inBaseSet=False
        self.currentCam = 'cam17'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[17]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[17] = time.time()

    def fullscreen18(self):
        self.inBaseSet=False
        self.currentCam = 'cam18'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[18]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[18] = time.time()

    def fullscreen19(self):
        self.inBaseSet=False
        self.currentCam = 'cam19'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[19]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[19] = time.time()

    def fullscreen20(self):
        self.inBaseSet=False
        self.currentCam = 'cam20'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[20]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[20] = time.time()

    def fullscreen21(self):
        self.inBaseSet=False
        self.currentCam = 'cam21'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[21]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[21] = time.time()

    def fullscreen22(self):
        self.inBaseSet=False
        self.currentCam = 'cam22'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[22]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[22] = time.time()

    def fullscreen23(self):
        self.inBaseSet=False
        self.currentCam = 'cam23'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[23]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[23] = time.time()

    def fullscreen24(self):
        self.inBaseSet=False
        self.currentCam = 'cam24'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[24]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[24] = time.time()

    def fullscreen25(self):
        self.inBaseSet=False
        self.currentCam = 'cam25'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[25]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[25] = time.time()

    def fullscreen26(self):
        self.inBaseSet=False
        self.currentCam = 'cam26'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[26]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[26] = time.time()

    def fullscreen27(self):
        self.inBaseSet=False
        self.currentCam = 'cam27'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[27]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[27] = time.time()

    def fullscreen28(self):
        self.inBaseSet=False
        self.currentCam = 'cam28'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[28]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[28] = time.time()

    def fullscreen29(self):
        self.inBaseSet=False
        self.currentCam = 'cam29'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[29]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[29] = time.time()

    def fullscreen30(self):
        self.inBaseSet=False
        self.currentCam = 'cam30'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[30]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[30] = time.time()

    def fullscreen31(self):
        self.inBaseSet=False
        self.currentCam = 'cam31'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[31]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[31] = time.time()

    def fullscreen32(self):
        self.currentCam = 'cam32'
        self.loadCameraSet()
        self.setLayerCorlr()
        
        now = time.time()
        if now - self.dclickTime[32]  < 0.3:
            self.inFullScreenMode = True
            self.resizeCamers(self.currentCam   , self.camDropWidgets)
        self.dclickTime[32] = time.time()