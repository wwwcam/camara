import cv2 
import imutils
from PySide2.QtWidgets import QApplication, QMainWindow , QMessageBox ,QLabel ,QWidget, QSpinBox
from PySide2 import QtUiTools
from PySide2.QtCore import QTimer,QObject,Signal,QTime
from PySide2.QtGui import QColor
from PySide2 import QtGui ,QtWidgets ,QtCore
from PySide2.QtWidgets import * 
from PySide2.QtGui import * 
from PySide2.QtCore import * 

class vplayer():
    def __init__(self):
        self.video = cv2.VideoCapture("./test.mp4")

    def playV1(self):
        if self.video.get(cv2.CAP_PROP_POS_FRAMES) == self.video.get(cv2.CAP_PROP_FRAME_COUNT):
            self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        
        ret, frame = self.video.read()
        if ret:
            if self.ui.cmraBt_01.iconSize() != self.ui.cmraBt_01.size():
                self.ui.cmraBt_01.setIconSize(self.ui.cmraBt_01.size())
                self.ui.cmraBt_02.setIconSize(self.ui.cmraBt_02.size())                
                self.ui.cmraBt_03.setIconSize(self.ui.cmraBt_03.size())                
                self.ui.cmraBt_04.setIconSize(self.ui.cmraBt_04.size())                
                self.ui.cmraBt_05.setIconSize(self.ui.cmraBt_05.size())                
                self.ui.cmraBt_06.setIconSize(self.ui.cmraBt_06.size())                
                self.ui.cmraBt_07.setIconSize(self.ui.cmraBt_07.size())                
                self.ui.cmraBt_08.setIconSize(self.ui.cmraBt_08.size())                
                self.ui.cmraBt_09.setIconSize(self.ui.cmraBt_09.size())                
                self.ui.cmraBt_10.setIconSize(self.ui.cmraBt_10.size())                
                self.ui.cmraBt_11.setIconSize(self.ui.cmraBt_11.size())                
                self.ui.cmraBt_12.setIconSize(self.ui.cmraBt_12.size())                
                self.ui.cmraBt_13.setIconSize(self.ui.cmraBt_13.size())                
                self.ui.cmraBt_14.setIconSize(self.ui.cmraBt_14.size())                
                self.ui.cmraBt_15.setIconSize(self.ui.cmraBt_15.size())                
                self.ui.cmraBt_16.setIconSize(self.ui.cmraBt_16.size())                
                self.ui.cmraBt_17.setIconSize(self.ui.cmraBt_17.size())                
                self.ui.cmraBt_18.setIconSize(self.ui.cmraBt_18.size())                
                self.ui.cmraBt_19.setIconSize(self.ui.cmraBt_19.size())                
                self.ui.cmraBt_20.setIconSize(self.ui.cmraBt_20.size())                
                self.ui.cmraBt_21.setIconSize(self.ui.cmraBt_21.size())                
                self.ui.cmraBt_22.setIconSize(self.ui.cmraBt_22.size())                
                self.ui.cmraBt_23.setIconSize(self.ui.cmraBt_23.size())                
                self.ui.cmraBt_24.setIconSize(self.ui.cmraBt_24.size())                
                self.ui.cmraBt_25.setIconSize(self.ui.cmraBt_25.size())                
                self.ui.cmraBt_26.setIconSize(self.ui.cmraBt_26.size())                
                self.ui.cmraBt_27.setIconSize(self.ui.cmraBt_27.size())                
                self.ui.cmraBt_28.setIconSize(self.ui.cmraBt_28.size())                
                self.ui.cmraBt_29.setIconSize(self.ui.cmraBt_29.size())                
                self.ui.cmraBt_30.setIconSize(self.ui.cmraBt_30.size())                
                self.ui.cmraBt_31.setIconSize(self.ui.cmraBt_31.size())                
                self.ui.cmraBt_32.setIconSize(self.ui.cmraBt_32.size())                
                self.ui.cmraBt_33.setIconSize(self.ui.cmraBt_33.size())                
                self.ui.cmraBt_34.setIconSize(self.ui.cmraBt_34.size())                
                self.ui.cmraBt_35.setIconSize(self.ui.cmraBt_35.size())                
                self.ui.cmraBt_36.setIconSize(self.ui.cmraBt_36.size())

            frame = imutils.resize(frame , height = self.ui.cmraBt_01.size().height()-10 )
            bytesPerLine = 3 * frame.shape[1]
            image = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], bytesPerLine  , QtGui.QImage.Format_RGB888).rgbSwapped()
            self.ui.cmraBt_01.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_02.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_03.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_04.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_05.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_06.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_07.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_08.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_09.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_10.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_11.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_12.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_13.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_14.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_15.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_16.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_17.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_18.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_19.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_20.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_21.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_22.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_23.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_24.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_25.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_26.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_27.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_28.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_29.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_30.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_31.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_32.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_33.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_34.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_35.setIcon(QPixmap.fromImage(image))                
            self.ui.cmraBt_36.setIcon(QPixmap.fromImage(image))