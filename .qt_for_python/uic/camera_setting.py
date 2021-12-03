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


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(313, 633)
        self.widget_9 = QWidget(Form)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setEnabled(True)
        self.widget_9.setGeometry(QRect(0, 0, 311, 631))
        self.widget_9.setMouseTracking(False)
        self.widget_9.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.sens_label_7 = QLabel(self.widget_9)
        self.sens_label_7.setObjectName(u"sens_label_7")
        self.sens_label_7.setGeometry(QRect(81, 494, 65, 21))
        self.sens_label_7.setStyleSheet(u"font: 75 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.ip_lineEdit_7 = QLineEdit(self.widget_9)
        self.ip_lineEdit_7.setObjectName(u"ip_lineEdit_7")
        self.ip_lineEdit_7.setGeometry(QRect(152, 376, 150, 20))
        self.ip_lineEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.foco_label_7 = QLabel(self.widget_9)
        self.foco_label_7.setObjectName(u"foco_label_7")
        self.foco_label_7.setGeometry(QRect(100, 522, 43, 21))
        self.foco_label_7.setStyleSheet(u"font: 75 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.camera_lineEdit_7 = QLineEdit(self.widget_9)
        self.camera_lineEdit_7.setObjectName(u"camera_lineEdit_7")
        self.camera_lineEdit_7.setGeometry(QRect(152, 403, 150, 20))
        self.camera_lineEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.foco_horizontalSlider_7 = QSlider(self.widget_9)
        self.foco_horizontalSlider_7.setObjectName(u"foco_horizontalSlider_7")
        self.foco_horizontalSlider_7.setGeometry(QRect(152, 522, 150, 22))
        self.foco_horizontalSlider_7.setOrientation(Qt.Horizontal)
        self.loca_label_7 = QLabel(self.widget_9)
        self.loca_label_7.setObjectName(u"loca_label_7")
        self.loca_label_7.setGeometry(QRect(80, 430, 63, 21))
        self.loca_label_7.setStyleSheet(u"font: 75 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.sens_horizontalSlider_7 = QSlider(self.widget_9)
        self.sens_horizontalSlider_7.setObjectName(u"sens_horizontalSlider_7")
        self.sens_horizontalSlider_7.setGeometry(QRect(152, 494, 150, 22))
        self.sens_horizontalSlider_7.setOrientation(Qt.Horizontal)
        self.memo_textEdit_7 = QTextEdit(self.widget_9)
        self.memo_textEdit_7.setObjectName(u"memo_textEdit_7")
        self.memo_textEdit_7.setGeometry(QRect(152, 550, 151, 71))
        self.memo_textEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.ip_label_7 = QLabel(self.widget_9)
        self.ip_label_7.setObjectName(u"ip_label_7")
        self.ip_label_7.setGeometry(QRect(130, 376, 16, 21))
        self.ip_label_7.setStyleSheet(u"font: 75 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.loca_lineEdit_7 = QLineEdit(self.widget_9)
        self.loca_lineEdit_7.setObjectName(u"loca_lineEdit_7")
        self.loca_lineEdit_7.setGeometry(QRect(152, 430, 150, 20))
        self.loca_lineEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.memo_label_7 = QLabel(self.widget_9)
        self.memo_label_7.setObjectName(u"memo_label_7")
        self.memo_label_7.setGeometry(QRect(100, 550, 48, 21))
        self.memo_label_7.setStyleSheet(u"font: 75 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.zoom_label_7 = QLabel(self.widget_9)
        self.zoom_label_7.setObjectName(u"zoom_label_7")
        self.zoom_label_7.setGeometry(QRect(100, 466, 43, 21))
        self.zoom_label_7.setStyleSheet(u"font: 75 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.zoom_horizontalSlider_7 = QSlider(self.widget_9)
        self.zoom_horizontalSlider_7.setObjectName(u"zoom_horizontalSlider_7")
        self.zoom_horizontalSlider_7.setGeometry(QRect(152, 466, 150, 22))
        self.zoom_horizontalSlider_7.setOrientation(Qt.Horizontal)
        self.iconBt_7 = QPushButton(self.widget_9)
        self.iconBt_7.setObjectName(u"iconBt_7")
        self.iconBt_7.setGeometry(QRect(0, 0, 261, 211))
        self.iconBt_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 11pt \"Agency FB\";\n"
"font: 16pt \"Agency FB\";")
        icon = QIcon()
        icon.addFile(u"../../../.designer/backup/datas/images/settingTransPb.png", QSize(), QIcon.Normal, QIcon.Off)
        self.iconBt_7.setIcon(icon)
        self.iconBt_7.setIconSize(QSize(200, 200))
        self.camera__label_7 = QLabel(self.widget_9)
        self.camera__label_7.setObjectName(u"camera__label_7")
        self.camera__label_7.setGeometry(QRect(90, 403, 55, 21))
        self.camera__label_7.setStyleSheet(u"font: 75 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.sens_label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">Sensitive</p></body></html>", None))
        self.foco_label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">Focos</p></body></html>", None))
        self.loca_label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">Location</p><p><br/></p></body></html>", None))
        self.ip_label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">Ip</p></body></html>", None))
        self.memo_label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">Memo</p></body></html>", None))
        self.zoom_label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">Zoom</p></body></html>", None))
        self.iconBt_7.setText(QCoreApplication.translate("Form", u"icon", None))
        self.camera__label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">Camera</p></body></html>", None))
    # retranslateUi

