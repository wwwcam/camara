import cv2 
import imutils
import traceback
import numpy as np
import time
import random
import requests
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
import os




def saveVideo(cam , savepath , frames ):
    print("save video start")
    width , height = frames[0][0].shape[1]*2 , frames[0][0].shape[0]
    lc = time.localtime()
    today = f"{lc[0]:02d}{lc[1]:02d}{lc[2]:02d}"
    now = f"{lc[3]:02d}{lc[4]:02d}{lc[5]:02d}"
    if os.path.isdir(savepath) == False:
        os.mkdir(savepath)
    if os.path.isdir(savepath+"/"+cam) == False:
        os.mkdir(savepath+"/"+cam)
    if os.path.isdir(savepath+"/" + cam + "/" +today) == False:
        os.mkdir(savepath+"/" + cam + "/" +today)
    fullsavename = os.path.abspath(savepath+"/" + cam + "/" +today+"/"+now+".avi")
    writer = cv2.VideoWriter(fullsavename, cv2.VideoWriter_fourcc('M','J','P','G'), int(round(len(frames)/10)) , (width, height))
    print("frames" , len(frames),int(round(len(frames)/10)))
    for ff in frames:
        img = cv2.hconcat((ff[0],ff[1]))
        writer.write(img)
    writer.release()



def playVideo(cam , name , video,frameBuff,errframes , contStack , Q,savepath,countMem,sens,memory,framCnt,errtime,writer):
    conSize = 1005 - int((sens/100.0) * 1000) 
    blurSize = 10 -int(10 * (sens/100.0))
    frd = None
    ret, frame = video.read()
    if type(frame) != type(None):
        frame = imutils.resize(frame , width = 720)
        frame = cv2.GaussianBlur(frame,(5,5),0)
        if Q.empty():
            if ret:
                frameDist = 5
                frameBuff.append(frame)
                if len(frameBuff) >= frameDist:
                    fr1 = frameBuff[0]
                    fr1 = cv2.cvtColor(fr1, cv2.COLOR_BGR2GRAY)
                    fr2 = frameBuff[-1]
                    fr2 = cv2.cvtColor(fr2, cv2.COLOR_BGR2GRAY)

                    frd = cv2.absdiff(fr1, fr2)
                    (T, frd) = cv2.threshold(frd, 30, 255, cv2.THRESH_BINARY)

                    contours, hierarchy = cv2.findContours(frd, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)    
                    image_color = frameBuff[0].copy()
                    zeros = np.zeros(image_color.shape, np.uint8)    
                    for cnt in contours:
                        (x, y, w, h) = cv2.boundingRect(cnt)
                        area = cv2.contourArea(cnt)
                        if conSize < area < 5000:
                            contStack.append(cnt)
                    cv2.fillPoly(zeros, pts =contStack, color=(0,255,100))
                    zGray = cv2.cvtColor(zeros, cv2.COLOR_BGR2GRAY)
                    (T, zThr) = cv2.threshold(zGray, 50, 255, cv2.THRESH_BINARY)
                    contours2, hierarchy = cv2.findContours(zThr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
                    zeros2 = np.zeros(image_color.shape, np.uint8)   
                    cv2.fillPoly(zeros2, pts =contours2, color=(0,255,100))
                    tmpcnts = []
                    for cnt in contours2:
                        (x, y, w, h) = cv2.boundingRect(cnt)
                        area = cv2.contourArea(cnt)
                        if conSize <area < 5000:
                            tmpcnts.append(cnt)
                     
                    if len(tmpcnts):
                        countMem[0] = True
                    if countMem[0]:
                        countMem[1] = time.time()
                        countMem[0] = False
                    if time.time() - countMem[1] > 5:
                        if countMem[0] == False and contStack:
                            contStack = tmpcnts = []
                            countMem[0] = False
                            #zeros = np.zeros(image_color.shape, np.uint8)
                            zeros2 = np.zeros(image_color.shape, np.uint8)     
                            countMem[1] = time.time()


                    contStack = tmpcnts
                    frameBuff = frameBuff[1:]
                    result = cv2.addWeighted(image_color, 0.8, zeros2, 0.3, 0)
                    memory.append(result)
                    memory = memory[-10:]
                    if name.strip() == '':
                        savename = cam
                    else:
                        savename = name.strip()
                    if len(tmpcnts) > 0:
                        Q.put( (result , True,savename))
                    else:
                        Q.put( (result , False,savename) )

                    if len(tmpcnts) > 0:
                        if errtime==-1:
                            errtime= time.time()
                            width , height = image_color[0].shape[1]*2 , image_color[0].shape[0]
                            #writer = cv2.VideoWriter(f'./test_{random.randint(0,9999)}.avi', cv2.VideoWriter_fourcc('M','J','P','G') ,25, (width, height))
                            #writer.write(result)
                        else:
                            
                            if time.time() - errtime > 10:
                                
                                
                                saveVideo(savename , savepath , errframes )
                                errframes = []
                                errtime =-1
                                #writer.release()
                                frameBuff = frameBuff[-frameDist : ]
                                contStack = []
                                tmpcnts = []
                                memory = []

                        errframes.append([image_color , result])

            return frameBuff,countMem,memory , errtime ,writer,errframes

class getImage():
    def __init__(self, ip):
        self.ip = ip
    def read(self):
        return requests.get(self.ip).content

def initCam(layer , cam , name ,ip,Q , Q2 , savepath , sens):
    if ip.endswith(".jpg" ):
        getimg = getImage(ip)
        video = getimg
    else:
        video = cv2.VideoCapture(ip)
    frams = None
    loops = True
    frameBuff = []
    contStack = []
    writer = None
    memory = []
    cnt = 0
    errtime = -1
    countMem = [ False , 0]
    errframes = []
    while loops:
        cnt+=1
        try:
            ret   = playVideo(cam  , name , video,frameBuff, errframes , contStack,Q,savepath,countMem,sens,memory , cnt , errtime,writer)
            if ret:
                frameBuff,countMem,memory,errtime,writer,errframes = ret
        except:
            print(cv2.CAP_FFMPEG , traceback.format_exc())
     
        if Q2.empty() == False:
            for qi in range(Q2.qsize()):
                d = Q2.get()
                if "quit" in d:
                    loops = False
                    Q.put( (np.zeros((1,1,3)) , False , cam))
                    return

                if "sens:" in d:
                    senstmp = int(d.split(":")[1])
                    if sens != senstmp:
                        frameBuff = []
                        contStack = []
                        sens = senstmp


class vplayer():
    def __init__(self):
        multiprocessing.freeze_support()
        self.frames = []
        self.contStack = []
        self.videoTime = time.time()
        self.videos = {}
        self.frames = {}
        self.ps = {}
        self.loops = {}
        self.frameBuff = {}
        self.Qs = {}
        self.ui.allStart.clicked.connect(self.allStart)
        self.ui.allStop.clicked.connect(self.allStop)
        
    
    def loadCamSet(self,layer , cam):
        ip = self.camSettings[layer][cam]["ip"]
        name = self.camSettings[layer][cam]["name"] 
        loc = self.camSettings[layer][cam]["location"]
        zoom = self.camSettings[layer][cam]["zoom"]
        sens = self.camSettings[layer][cam]["sens"]
        focus = self.camSettings[layer][cam]["focus"]
        memo = self.camSettings[layer][cam]["memo"]
        return ip , name , loc , zoom , sens , focus , memo

    def allStart(self, noask = False):
        
        if noask == False:
            reply = QMessageBox.question(self.ui, 'Message', '모니터링을 시작하시겠습니까?',
                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        else:
            reply = QMessageBox.Yes
        if reply == QMessageBox.Yes:
            self.allStoped = False
            for cam in self.cameras:
                if cam in self.ps:
                    if self.ps[cam].is_alive ():
                        self.ps[cam].terminate()
                self.Qs[cam] = [Queue() , Queue()]
                ip , name , loc , zoom , sens , focus , memo = self.loadCamSet(self.currentLayer ,cam )
                if ip:
                    self.ps[cam] = Process(target = initCam , args = (self.currentLayer ,cam , name , ip, self.Qs[cam][0] ,  self.Qs[cam][1] , self.savePath ,sens))
                    self.ps[cam].start()

    def allStop(self , noask = False):

        if noask == False:
            reply = QMessageBox.question(self.ui, 'Message', '모니터링을 종료하시겠습니까?',
                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        else:
            reply = QMessageBox.Yes

        if reply == QMessageBox.Yes:
            self.allStoped = True
            for cam in self.cameras:
                if cam in self.ps:
                    if self.ps[cam].is_alive ():
                        self.Qs[cam][1].put(("quit" , False , ""))
                        self.stopVideos = 1
                        name = self.camSettings[self.currentLayer][cam]["name"]
                        btn = self.cameras[cam]
                        btn.setStyleSheet(self.emptyCam) 
                        if name.strip() == '':
                            btn.setText(cam)
                        else:
                            btn.setText(name)
                        #self.ps[cam].terminate()


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
                for btn in self.cameras:
                    if btn.size().height() == 891:
                        height = 891
                        break
                image_color = cv2.addWeighted(image_color, 0.8, zeros2, 0.3, 0)
                if frame.shape != (1,1,3):
                    frame = imutils.resize(image_color , height = height-10 )
                #frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
                bytesPerLine = 3 * frame.shape[1]
                image = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], bytesPerLine  , QtGui.QImage.Format_RGB888).rgbSwapped()
                for btn in self.cameras:
                    btn.setIcon(QPixmap.fromImage(image))   
                    break 

                for btn in self.cameras:
                    if btn.iconSize() != btn.size():
                        btn.setIconSize(btn.size())
                        break