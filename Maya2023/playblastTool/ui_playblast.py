# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'playblastTHLSrN.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                          QRect, QSize, QUrl, Qt, )
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import CustomWidgets
import os

iconDir = os.path.dirname(__file__)
print(iconDir)

import importlib
importlib.reload(CustomWidgets)

from CustomWidgets import CheckableCombobox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(426, 710)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_11 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.playblastGB = QGroupBox(self.centralwidget)
        self.playblastGB.setObjectName(u"playblastGB")
        self.verticalLayout_9 = QVBoxLayout(self.playblastGB)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout3 = QHBoxLayout()
        self.horizontalLayout3.setObjectName(u"horizontalLayout3")
        self.pbCameras = QLabel(self.playblastGB)
        self.pbCameras.setObjectName(u"pbCameras")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pbCameras.sizePolicy().hasHeightForWidth())
        self.pbCameras.setSizePolicy(sizePolicy1)

        self.horizontalLayout3.addWidget(self.pbCameras)

        self.cameraComboBox = CheckableCombobox(self.playblastGB)
        self.cameraComboBox.setObjectName(u"cameraComboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cameraComboBox.sizePolicy().hasHeightForWidth())
        self.cameraComboBox.setSizePolicy(sizePolicy2)

        self.horizontalLayout3.addWidget(self.cameraComboBox)

        self.refreshCamerasButton = QToolButton(self.playblastGB)
        self.refreshCamerasButton.setObjectName(u"refreshCamerasButton")
        icon = QIcon()
        icon.addFile(r"C:\Users\saura\pyTools\Shared\icons\refreshIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshCamerasButton.setIcon(icon)

        self.horizontalLayout3.addWidget(self.refreshCamerasButton)


        self.verticalLayout_9.addLayout(self.horizontalLayout3)

        self.stitchCheckBox = QCheckBox(self.playblastGB)
        self.stitchCheckBox.setObjectName(u"stitchCheckBox")

        self.verticalLayout_9.addWidget(self.stitchCheckBox)

        self.verticalLayout_11.addWidget(self.playblastGB)

        self.FrameRangeGB = QGroupBox(self.centralwidget)
        self.FrameRangeGB.setObjectName(u"FrameRangeGB")
        self.verticalLayout = QVBoxLayout(self.FrameRangeGB)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.rangeSliderRB = QRadioButton(self.FrameRangeGB)
        self.rangeSliderRB.setObjectName(u"rangeSliderRB")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.rangeSliderRB.sizePolicy().hasHeightForWidth())
        self.rangeSliderRB.setSizePolicy(sizePolicy3)
        self.rangeSliderRB.setMinimumSize(QSize(0, 22))

        self.verticalLayout.addWidget(self.rangeSliderRB)

        self.timeSliderRB = QRadioButton(self.FrameRangeGB)
        self.timeSliderRB.setObjectName(u"timeSliderRB")
        self.timeSliderRB.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.timeSliderRB.sizePolicy().hasHeightForWidth())
        self.timeSliderRB.setSizePolicy(sizePolicy4)
        self.timeSliderRB.setMinimumSize(QSize(0, 22))

        self.verticalLayout.addWidget(self.timeSliderRB)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.customRB = QRadioButton(self.FrameRangeGB)
        self.customRB.setObjectName(u"customRB")

        self.horizontalLayout_2.addWidget(self.customRB)

        self.startFrameLabel = QLabel(self.FrameRangeGB)
        self.startFrameLabel.setObjectName(u"startFrameLabel")
        self.startFrameLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.startFrameLabel)

        self.startFrameSB = QSpinBox(self.FrameRangeGB)
        self.startFrameSB.setObjectName(u"startFrameSB")
        self.startFrameSB.setMinimum(-10000)
        self.startFrameSB.setMaximum(10000)

        self.horizontalLayout_2.addWidget(self.startFrameSB)

        self.line = QFrame(self.FrameRangeGB)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.endFrameLabel = QLabel(self.FrameRangeGB)
        self.endFrameLabel.setObjectName(u"endFrameLabel")
        self.endFrameLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.endFrameLabel)

        self.endFrameSB = QSpinBox(self.FrameRangeGB)
        self.endFrameSB.setObjectName(u"endFrameSB")
        self.endFrameSB.setMinimum(-100000)
        self.endFrameSB.setMaximum(100000)

        self.horizontalLayout_2.addWidget(self.endFrameSB)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bookmarkRB = QRadioButton(self.FrameRangeGB)
        self.bookmarkRB.setObjectName(u"bookmarkRB")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.bookmarkRB.sizePolicy().hasHeightForWidth())
        self.bookmarkRB.setSizePolicy(sizePolicy5)

        self.horizontalLayout.addWidget(self.bookmarkRB)

        self.bookmarkComboBox = CheckableCombobox(self.FrameRangeGB)
        self.bookmarkComboBox.setObjectName(u"bookmarkComboBox")
        sizePolicy2.setHeightForWidth(self.bookmarkComboBox.sizePolicy().hasHeightForWidth())
        self.bookmarkComboBox.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.bookmarkComboBox)

        self.bookmarkRefreshButton = QToolButton(self.FrameRangeGB)
        self.bookmarkRefreshButton.setObjectName(u"bookmarkRefreshButton")
        self.bookmarkRefreshButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.bookmarkRefreshButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_11.addWidget(self.FrameRangeGB)

        self.blastSettingsGB = QGroupBox(self.centralwidget)
        self.blastSettingsGB.setObjectName(u"blastSettingsGB")
        sizePolicy4.setHeightForWidth(self.blastSettingsGB.sizePolicy().hasHeightForWidth())
        self.blastSettingsGB.setSizePolicy(sizePolicy4)
        self.verticalLayout_7 = QVBoxLayout(self.blastSettingsGB)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.settingsTableWidget = QTableWidget(self.blastSettingsGB)
        if (self.settingsTableWidget.columnCount() < 2):
            self.settingsTableWidget.setColumnCount(2)
        self.settingTab = QTableWidgetItem()
        self.settingsTableWidget.setHorizontalHeaderItem(0, self.settingTab)
        self.valueTab = QTableWidgetItem()
        self.settingsTableWidget.setHorizontalHeaderItem(1, self.valueTab)
        self.settingsTableWidget.setObjectName(u"settingsTableWidget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy6.setHeightForWidth(self.settingsTableWidget.sizePolicy().hasHeightForWidth())
        self.settingsTableWidget.setSizePolicy(sizePolicy6)
        self.settingsTableWidget.setMinimumSize(QSize(0, 350))
        self.settingsTableWidget.setShowGrid(False)

        self.verticalLayout_7.addWidget(self.settingsTableWidget)

        self.horizontalLayout2 = QHBoxLayout()
        self.horizontalLayout2.setObjectName(u"horizontalLayout2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout2.addItem(self.horizontalSpacer)

        self.addSettingsButton = QPushButton(self.blastSettingsGB)
        self.addSettingsButton.setObjectName(u"addSettingsButton")

        self.horizontalLayout2.addWidget(self.addSettingsButton)

        self.setToDefaultButton = QPushButton(self.blastSettingsGB)
        self.setToDefaultButton.setObjectName(u"setToDefaultButton")

        self.horizontalLayout2.addWidget(self.setToDefaultButton)


        self.verticalLayout_7.addLayout(self.horizontalLayout2)


        self.verticalLayout_11.addWidget(self.blastSettingsGB)

        self.blastProperties = QGroupBox(self.centralwidget)
        self.blastProperties.setObjectName(u"blastProperties")
        self.verticalLayout_6 = QVBoxLayout(self.blastProperties)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout1 = QHBoxLayout()
        self.horizontalLayout1.setObjectName(u"horizontalLayout1")
        self.resolutionGB = QGroupBox(self.blastProperties)
        self.resolutionGB.setObjectName(u"resolutionGB")
        self.horizontalLayout_9 = QHBoxLayout(self.resolutionGB)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lowQuality = QRadioButton(self.resolutionGB)
        self.lowQuality.setObjectName(u"lowQuality")

        self.horizontalLayout_9.addWidget(self.lowQuality)

        self.hdQuality = QRadioButton(self.resolutionGB)
        self.hdQuality.setObjectName(u"hdQuality")

        self.horizontalLayout_9.addWidget(self.hdQuality)

        self.fhdQuality = QRadioButton(self.resolutionGB)
        self.fhdQuality.setObjectName(u"fhdQuality")

        self.horizontalLayout_9.addWidget(self.fhdQuality)


        self.horizontalLayout1.addWidget(self.resolutionGB)

        self.frameRateGB = QGroupBox(self.blastProperties)
        self.frameRateGB.setObjectName(u"frameRateGB")
        self.horizontalLayout_10 = QHBoxLayout(self.frameRateGB)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.fps30RB = QRadioButton(self.frameRateGB)
        self.fps30RB.setObjectName(u"fps30RB")

        self.horizontalLayout_10.addWidget(self.fps30RB)

        self.fps60RB = QRadioButton(self.frameRateGB)
        self.fps60RB.setObjectName(u"fps60RB")

        self.horizontalLayout_10.addWidget(self.fps60RB)


        self.horizontalLayout1.addWidget(self.frameRateGB)

        self.formatGB = QGroupBox(self.blastProperties)
        self.formatGB.setObjectName(u"formatGB")
        self.horizontalLayout_11 = QHBoxLayout(self.formatGB)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.aviRB = QRadioButton(self.formatGB)
        self.aviRB.setObjectName(u"aviRB")

        self.horizontalLayout_11.addWidget(self.aviRB)

        self.movRB = QRadioButton(self.formatGB)
        self.movRB.setObjectName(u"movRB")

        self.horizontalLayout_11.addWidget(self.movRB)

        self.pngRB = QRadioButton(self.formatGB)
        self.pngRB.setObjectName(u"pngRB")

        self.horizontalLayout_11.addWidget(self.pngRB)


        self.horizontalLayout1.addWidget(self.formatGB)


        self.verticalLayout_6.addLayout(self.horizontalLayout1)


        self.verticalLayout_11.addWidget(self.blastProperties)

        self.extraOptionsGB = QGroupBox(self.centralwidget)
        self.extraOptionsGB.setObjectName(u"extraOptionsGB")
        self.horizontalLayout_3 = QHBoxLayout(self.extraOptionsGB)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.offScreenCheckBox = QCheckBox(self.extraOptionsGB)
        self.offScreenCheckBox.setObjectName(u"offScreenCheckBox")

        self.horizontalLayout_3.addWidget(self.offScreenCheckBox)

        self.openPBCheckBox = QCheckBox(self.extraOptionsGB)
        self.openPBCheckBox.setObjectName(u"openPBCheckBox")

        self.horizontalLayout_3.addWidget(self.openPBCheckBox)

        self.ornamentsCheckBox = QCheckBox(self.extraOptionsGB)
        self.ornamentsCheckBox.setObjectName(u"ornamentsCheckBox")

        self.horizontalLayout_3.addWidget(self.ornamentsCheckBox)

        self.verticalLayout_11.addWidget(self.extraOptionsGB)

        self.saveBlast = QGroupBox(self.centralwidget)
        self.saveBlast.setObjectName(u"saveBlast")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.saveBlast.sizePolicy().hasHeightForWidth())
        self.saveBlast.setSizePolicy(sizePolicy7)
        self.verticalLayout_8 = QVBoxLayout(self.saveBlast)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout4 = QHBoxLayout()
        self.horizontalLayout4.setObjectName(u"horizontalLayout4")
        self.label = QLabel(self.saveBlast)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.horizontalLayout4.addWidget(self.label)

        self.savePathTextEdit = QTextEdit(self.saveBlast)
        self.savePathTextEdit.setObjectName(u"savePathTextEdit")
        sizePolicy2.setHeightForWidth(self.savePathTextEdit.sizePolicy().hasHeightForWidth())
        self.savePathTextEdit.setSizePolicy(sizePolicy2)
        self.savePathTextEdit.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout4.addWidget(self.savePathTextEdit)

        self.browseButton = QPushButton(self.saveBlast)
        self.browseButton.setObjectName(u"browseButton")

        self.horizontalLayout4.addWidget(self.browseButton)


        self.verticalLayout_8.addLayout(self.horizontalLayout4)

        self.playblastButton = QPushButton(self.saveBlast)
        self.playblastButton.setObjectName(u"playblastButton")

        self.verticalLayout_8.addWidget(self.playblastButton)


        self.verticalLayout_11.addWidget(self.saveBlast)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 426, 22))
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Playblast Tool", None))
        self.playblastGB.setTitle(QCoreApplication.translate("MainWindow", u"Playblast", None))
        self.pbCameras.setText(QCoreApplication.translate("MainWindow", u"Select Camera", None))
        self.refreshCamerasButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.stitchCheckBox.setText(QCoreApplication.translate("MainWindow",
                                                               u"Single Tiled Playblast",
                                                               None))
        self.FrameRangeGB.setTitle(QCoreApplication.translate("MainWindow", u"Frame Range", None))
        self.rangeSliderRB.setText(QCoreApplication.translate("MainWindow", u"Range Slider", None))
        self.timeSliderRB.setText(QCoreApplication.translate("MainWindow", u"Time Slider", None))
        self.customRB.setText(QCoreApplication.translate("MainWindow", u"Custom", None))
        self.startFrameLabel.setText(QCoreApplication.translate("MainWindow", u"Start:", None))
        self.endFrameLabel.setText(QCoreApplication.translate("MainWindow", u"End", None))
        self.bookmarkRB.setText(QCoreApplication.translate("MainWindow", u"Bookmarks", None))
        self.bookmarkRefreshButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.blastSettingsGB.setTitle(QCoreApplication.translate("MainWindow", u"Blast Settings", None))
        self.addSettingsButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.setToDefaultButton.setText(QCoreApplication.translate("MainWindow", u"Default Settings", None))
        self.blastProperties.setTitle(QCoreApplication.translate("MainWindow", u"Output Properties", None))
        self.resolutionGB.setTitle(QCoreApplication.translate("MainWindow", u"Resolution", None))
        self.lowQuality.setText(QCoreApplication.translate("MainWindow", u"480p", None))
        self.hdQuality.setText(QCoreApplication.translate("MainWindow", u"720p", None))
        self.fhdQuality.setText(QCoreApplication.translate("MainWindow", u"1080p", None))
        self.frameRateGB.setTitle(QCoreApplication.translate("MainWindow", u"Frame Rate", None))
        self.fps30RB.setText(QCoreApplication.translate("MainWindow", u"30fps", None))
        self.fps60RB.setText(QCoreApplication.translate("MainWindow", u"60fps", None))
        self.formatGB.setTitle(QCoreApplication.translate("MainWindow", u"Format", None))
        self.aviRB.setText(QCoreApplication.translate("MainWindow", u".avi", None))
        self.movRB.setText(QCoreApplication.translate("MainWindow", u".mov", None))
        self.pngRB.setText(QCoreApplication.translate("MainWindow", u".png Seq", None))
        self.extraOptionsGB.setTitle(
            QCoreApplication.translate("MainWindow", u"Extra Options", None))
        self.offScreenCheckBox.setText(
            QCoreApplication.translate("MainWindow", u"Off Screen Blast",
                                       None))
        self.openPBCheckBox.setText(
            QCoreApplication.translate("MainWindow", u"Open Playblast", None))
        self.ornamentsCheckBox.setText(
            QCoreApplication.translate("MainWindow", u"Show Ornaments", None))
        self.saveBlast.setTitle(QCoreApplication.translate("MainWindow", u"Save Blast", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.browseButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.playblastButton.setText(QCoreApplication.translate("MainWindow", u"Playblast", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.settingTab = self.settingsTableWidget.horizontalHeaderItem(0)
        self.settingTab.setText(
            QCoreApplication.translate("MainWindow", u"Settings Name", None))
        self.valueTab = self.settingsTableWidget.horizontalHeaderItem(1)
        self.valueTab.setText(
            QCoreApplication.translate("MainWindow", u"Vaule", None))
        header = self.settingsTableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
    # retranslateUi








