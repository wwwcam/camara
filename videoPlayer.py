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
            frame = imutils.resize(frame , height = self.ui.cmraBt_01.size().height()-10 )
                
            bytesPerLine = 3 * frame.shape[1]
            image = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], bytesPerLine  , QtGui.QImage.Format_RGB888).rgbSwapped()
            self.ui.cmraBt_01.setIcon(QPixmap.fromImage(image))