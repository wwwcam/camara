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

class vplayer():
    def __init__(self,parent):
        self.video = cv2.VideoCapture("./test.mp4")
        self.frames = []
        self.contStack = []
        self.videoTime = time.time()
        self.parent = parent

    def playV1(self):
        if self.video.get(cv2.CAP_PROP_POS_FRAMES) == self.video.get(cv2.CAP_PROP_FRAME_COUNT):
            self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            self.frames = []
            self.contStack = []
        frd = None
        ret, frame = self.video.read()
        
        
        if ret:
            if time.time() - self.videoTime > 6:
                self.videoTime =time.time()
            self.filterSize = 7
            self.frameDist = 10
            self.frames.append(frame)
            if len(self.frames) > self.frameDist:
                fr1 = self.frames[0]
                fr1 = cv2.cvtColor(fr1, cv2.COLOR_BGR2GRAY)
                fr2 = self.frames[-1]
                fr2 = cv2.cvtColor(fr2, cv2.COLOR_BGR2GRAY)

                frd = cv2.absdiff(fr1, fr2)
                (T, frd) = cv2.threshold(frd, 30, 255, cv2.THRESH_BINARY)

                contours, hierarchy = cv2.findContours(frd, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)    
                image_color = self.frames[0].copy()
                zeros = np.zeros(image_color.shape, np.uint8)    
                for cnt in contours:
                    (x, y, w, h) = cv2.boundingRect(cnt)
                    area = cv2.contourArea(cnt)
                    if 200<area < 5000:
                        self.contStack.append(cnt)
                #cv2.drawContours(zeros, self.contStack, -1, (0,0,255), 1)
                cv2.fillPoly(zeros, pts =self.contStack, color=(0,255,255))
                zGray = cv2.cvtColor(zeros, cv2.COLOR_BGR2GRAY)
                (T, zThr) = cv2.threshold(zGray, 50, 255, cv2.THRESH_BINARY)
                contours2, hierarchy = cv2.findContours(zThr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
                zeros2 = np.zeros(image_color.shape, np.uint8)   
                cv2.fillPoly(zeros2, pts =contours2, color=(0,255,255))
                self.contStack = contours2
                self.frames = self.frames[1:]

            if type(frd) != type(None):
                #
                height = 138
                for btn in self.parent.cameras:
                    if btn.size().height() == 891:
                        height = 891
                        break
                image_color = cv2.addWeighted(image_color, 0.8, zeros2, 0.3, 0)
                frame = imutils.resize(image_color , height = height-10 )
                #frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
                bytesPerLine = 3 * frame.shape[1]
                image = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], bytesPerLine  , QtGui.QImage.Format_RGB888).rgbSwapped()
                for btn in self.parent.cameras:
                    btn.setIcon(QPixmap.fromImage(image))   
                    break 

                for btn in self.parent.cameras:
                    if btn.iconSize() != btn.size():
                        btn.setIconSize(btn.size())
                        break
                