from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtUiTools

class Pannel(QWidget):
    def __init__(self, base=None , path=None , root = None):
        QWidget.__init__(self)
        self.root= root
        self.ui = QtUiTools.QUiLoader(parent=base).load(path ,base  )
        rMyIcon = QPixmap("./datas/images/setIcon.png")
        self.ui.iconBt_7.setIcon(QIcon(rMyIcon))
        self.ui.sens_horizontalSlider_7.valueChanged.connect(self.sensChange)

    def sensChange(self):
        if self.root.inBaseSet:
            val = self.root.camBaseSettings[self.root.baseCamNum]["sens"] = self.ui.sens_horizontalSlider_7.value()
        else:
            val  =self.root.camSettings[self.root.currentLayer][self.root.currentCam]["sens"] = self.ui.sens_horizontalSlider_7.value()
            if self.root.currentCam in self.root.Qs:
                self.root.Qs[self.root.currentCam][1].put(( "sens:"+str(val) , False , "")) 
        
        
