from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtUiTools

class Pannel(QWidget):
    def __init__(self, parent=None , path=None):
        QWidget.__init__(self)
        self.ui = QtUiTools.QUiLoader(parent=parent).load(path ,parent  )
        rMyIcon = QPixmap("./datas/images/setIcon.png")
        self.ui.iconBt_7.setIcon(QIcon(rMyIcon))