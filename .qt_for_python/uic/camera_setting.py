# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camera_setting.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import image_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(263, 869)
        self.widget_9 = QWidget(Form)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setEnabled(True)
        self.widget_9.setGeometry(QRect(0, 0, 261, 871))
        self.widget_9.setMouseTracking(False)
        self.widget_9.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.ip_lineEdit_7 = QLineEdit(self.widget_9)
        self.ip_lineEdit_7.setObjectName(u"ip_lineEdit_7")
        self.ip_lineEdit_7.setGeometry(QRect(100, 255, 150, 20))
        self.ip_lineEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.loca_label_7 = QLabel(self.widget_9)
        self.loca_label_7.setObjectName(u"loca_label_7")
        self.loca_label_7.setGeometry(QRect(30, 280, 63, 21))
        self.loca_label_7.setStyleSheet(u"font: 75 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memo_textEdit_7 = QTextEdit(self.widget_9)
        self.memo_textEdit_7.setObjectName(u"memo_textEdit_7")
        self.memo_textEdit_7.setGeometry(QRect(102, 400, 151, 71))
        self.memo_textEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.ip_label_7 = QLabel(self.widget_9)
        self.ip_label_7.setObjectName(u"ip_label_7")
        self.ip_label_7.setGeometry(QRect(20, 255, 71, 21))
        self.ip_label_7.setStyleSheet(u"font: 75 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.loca_lineEdit_7 = QLineEdit(self.widget_9)
        self.loca_lineEdit_7.setObjectName(u"loca_lineEdit_7")
        self.loca_lineEdit_7.setGeometry(QRect(100, 280, 150, 20))
        self.loca_lineEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.memo_label_7 = QLabel(self.widget_9)
        self.memo_label_7.setObjectName(u"memo_label_7")
        self.memo_label_7.setGeometry(QRect(50, 400, 48, 21))
        self.memo_label_7.setStyleSheet(u"font: 75 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.iconBt_7 = QPushButton(self.widget_9)
        self.iconBt_7.setObjectName(u"iconBt_7")
        self.iconBt_7.setGeometry(QRect(0, 0, 261, 211))
        self.iconBt_7.setStyleSheet(u"color: rgba(255, 255, 255);\n"
"background-color: rgba(222, 255, 254, 30);\n"
"font: 11pt \"Agency FB\";\n"
"font: 16pt \"Agency FB\";")
        icon = QIcon()
        icon.addFile(u"../../../.designer/backup/datas/images/settingTransPb.png", QSize(), QIcon.Normal, QIcon.Off)
        self.iconBt_7.setIcon(icon)
        self.iconBt_7.setIconSize(QSize(200, 200))
        self.camera__label_7 = QLabel(self.widget_9)
        self.camera__label_7.setObjectName(u"camera__label_7")
        self.camera__label_7.setGeometry(QRect(40, 230, 55, 21))
        self.camera__label_7.setStyleSheet(u"font: 75 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.saveButton = QPushButton(self.widget_9)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(10, 480, 81, 23))
        self.saveButton.setStyleSheet(u"background-color: rgba(43, 128, 255,100);")
        self.horizontalLayoutWidget = QWidget(self.widget_9)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(80, 310, 171, 24))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 75 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label)

        self.zoom_horizontalSlider_7 = QSlider(self.horizontalLayoutWidget)
        self.zoom_horizontalSlider_7.setObjectName(u"zoom_horizontalSlider_7")
        self.zoom_horizontalSlider_7.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.zoom_horizontalSlider_7)

        self.horizontalLayoutWidget_2 = QWidget(self.widget_9)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(80, 340, 171, 24))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 75 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.sens_horizontalSlider_7 = QSlider(self.horizontalLayoutWidget_2)
        self.sens_horizontalSlider_7.setObjectName(u"sens_horizontalSlider_7")
        self.sens_horizontalSlider_7.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.sens_horizontalSlider_7)

        self.horizontalLayoutWidget_3 = QWidget(self.widget_9)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(80, 370, 171, 24))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 75 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.foco_horizontalSlider_7 = QSlider(self.horizontalLayoutWidget_3)
        self.foco_horizontalSlider_7.setObjectName(u"foco_horizontalSlider_7")
        self.foco_horizontalSlider_7.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.foco_horizontalSlider_7)

        self.label_4 = QLabel(self.widget_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 310, 51, 22))
        self.label_4.setStyleSheet(u"font: 75 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.label_5 = QLabel(self.widget_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 340, 71, 22))
        self.label_5.setStyleSheet(u"font: 75 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.foco_label_7 = QLabel(self.widget_9)
        self.foco_label_7.setObjectName(u"foco_label_7")
        self.foco_label_7.setGeometry(QRect(30, 370, 43, 22))
        self.foco_label_7.setStyleSheet(u"font: 75 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.camera_lineEdit_7 = QLabel(self.widget_9)
        self.camera_lineEdit_7.setObjectName(u"camera_lineEdit_7")
        self.camera_lineEdit_7.setGeometry(QRect(100, 225, 151, 26))
        self.camera_lineEdit_7.setStyleSheet(u"font: 75 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        QWidget.setTabOrder(self.ip_lineEdit_7, self.loca_lineEdit_7)
        QWidget.setTabOrder(self.loca_lineEdit_7, self.zoom_horizontalSlider_7)
        QWidget.setTabOrder(self.zoom_horizontalSlider_7, self.sens_horizontalSlider_7)
        QWidget.setTabOrder(self.sens_horizontalSlider_7, self.foco_horizontalSlider_7)
        QWidget.setTabOrder(self.foco_horizontalSlider_7, self.memo_textEdit_7)
        QWidget.setTabOrder(self.memo_textEdit_7, self.saveButton)
        QWidget.setTabOrder(self.saveButton, self.iconBt_7)

        self.retranslateUi(Form)
        self.foco_horizontalSlider_7.valueChanged.connect(self.label_3.setNum)
        self.zoom_horizontalSlider_7.valueChanged.connect(self.label.setNum)
        self.sens_horizontalSlider_7.valueChanged.connect(self.label_2.setNum)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.loca_label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">Location</p><p><br/></p></body></html>", None))
        self.ip_label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">Address</p></body></html>", None))
        self.memo_label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">Memo</p></body></html>", None))
        self.iconBt_7.setText("")
        self.camera__label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">Camera</p></body></html>", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"Save", None))
        self.label.setText(QCoreApplication.translate("Form", u"00", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"00", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"00", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Zoom", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Sensitive ", None))
        self.foco_label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">Focos</p></body></html>", None))
        self.camera_lineEdit_7.setText("")
    # retranslateUi

