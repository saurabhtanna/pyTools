import maya.cmds as cmds
import sys
import os
import inspect

# Get the directory of the currently executing script
pbModulePath = os.path.dirname(inspect.getfile(inspect.currentframe()))

# Add the directory to sys.path if not already in there
if pbModulePath not in sys.path:
    sys.path.append(pbModulePath)

from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog,
                             QPushButton, QTableWidgetItem, QComboBox,
                             QAbstractItemView)
from PyQt5.QtCore import Qt, QEvent

import PlayblastCore
import ViewPortSettingsWidget
import importlib

importlib.reload(ViewPortSettingsWidget)
importlib.reload(PlayblastCore)


class PBTool(QMainWindow):

    def __init__(self):
        myPath = r'C:\Users\saura\pyTools\Maya2023\playblastTool'
        if myPath not in sys.path:
            sys.path.append(myPath)

        import ui_playblast
        import importlib
        importlib.reload(ui_playblast)

        super(PBTool, self).__init__()

        self.ui = ui_playblast.Ui_MainWindow()
        self.ui.setupUi(self)

        # Get Default and Saved UI values from VP JSON file
        self.defaultVPSettings = PlayblastCore.getDefaultVPSettings()
        self.savedVPSettings = PlayblastCore.getSavedVPSettings()

        # Setup UI
        self.ui.settingsTableWidget.verticalHeader().setVisible(False)
        self.ui.browseButton.clicked.connect(self.browseFiles)
        self.ui.savePathTextEdit.setText("C:/temp/DefaultPlayblast")
        self.refreshCameraCombobox()
        self.refreshBookmarkComboBox()
        self.radioButtonToggleWidgets()
        self.ui.hdQuality.setChecked(True)
        self.ui.fps30RB.setChecked(True)
        self.ui.aviRB.setChecked(True)
        self.ui.timeSliderRB.setChecked(True)



        #Setup Connections
        self.ui.refreshCamerasButton.clicked.connect(
            self.refreshCameraCombobox)
        self.ui.bookmarkRefreshButton.clicked.connect(
            self.refreshBookmarkComboBox)
        self.ui.addSettingsButton.clicked.connect(self.populateSettingsTable)
        self.ui.bookmarkRB.toggled.connect(self.radioButtonToggleWidgets)
        self.ui.customRB.toggled.connect(self.radioButtonToggleWidgets)
        self.ui.playblastButton.clicked.connect(self.playblastData)

    def browseFiles(self):
        """
        Adds browse functionality to the Browse button. Calls updateFilePath to
        update the File path text box.
        :return:
        """
        options = QFileDialog.Options()
        filePath = QFileDialog.getExistingDirectory(self,
                                                    "Select Save Location",
                                                    options=options)
        if filePath:
            self.ui.savePathTextEdit.setText(filePath)

    def getPBFilePath(self):
        """
        Read PB path and add the playblast name.
        :return:
        """
        pbFilePath = self.ui.savePathTextEdit.toPlainText()

        return pbFilePath

    def populateSettingsTable(self, vpSettings=None):
        """

        :param vpSettings:
        :return:
        """
        vpTable = self.ui.settingsTableWidget
        if not vpSettings:
            for settingName in self.savedVPSettings:
                rowPosition = self.ui.settingsTableWidget.rowCount()
                vpTable.insertRow(rowPosition)
                item = QTableWidgetItem(settingName)
                item.setTextAlignment(Qt.AlignCenter)
                vpTable.setItem(rowPosition, 0, item)

                if self.savedVPSettings[settingName][1] == 'boolean':
                    toggleItem = QTableWidgetItem('True')
                    toggleItem.setFlags(
                        Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    toggleItem.setCheckState(Qt.Unchecked)
                    vpTable.setItem(rowPosition, 1, toggleItem)
                if self.savedVPSettings[settingName][1] == 'list':
                    selectValue = QComboBox()
                    selectValue.installEventFilter(self)
                    selectValue.addItems(self.savedVPSettings[settingName][2])
                    vpTable.setCellWidget(rowPosition, 1, selectValue)

        vpTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        vpTable.setSelectionMode(QAbstractItemView.NoSelection)

    def radioButtonToggleWidgets(self):
        """

        :return:
        """
        self.ui.bookmarkComboBox.setEnabled(self.ui.bookmarkRB.isChecked())
        self.ui.bookmarkRefreshButton.setEnabled(self.ui.bookmarkRB.isChecked())
        self.ui.startFrameSB.setEnabled(self.ui.customRB.isChecked())
        self.ui.endFrameSB.setEnabled(self.ui.customRB.isChecked())


    def refreshCameraCombobox(self):
        """

        :param camList:
        :return:
        """
        self.ui.cameraComboBox.clear()
        camList = getCameraList()
        for cam in camList:
            self.ui.cameraComboBox.addItem(cam)

    def refreshBookmarkComboBox(self):
        """

        :return:
        """
        self.ui.bookmarkComboBox.clear()
        bookmarks = getBookmarksList()
        for bookmark in bookmarks:
            frameRange = cmds.getAttr(bookmark[1]+".timeRange")
            itemString = "{0} {1}".format(bookmark[0], frameRange[0])
            self.ui.bookmarkComboBox.addItem(itemString, bookmark[1])


    def getCheckedCameras(self):
        """

        :return:
        """
        camList = self.ui.cameraComboBox.getCheckedItems()
        return camList

    def getCheckedBookmarks(self):
        """

        :return:
        """
        bmList = self.ui.bookmarkComboBox.getCheckedData()
        return bmList

    def getFrameRange(self):
        """
        Checks the frame range mode and finds the range based on the mode.
        :return:
        """
        frameRange = []
        if self.ui.timeSliderRB.isChecked():
            print("timeslider")
            startFrame = cmds.playbackOptions(min=True, q=True)
            endFrame = cmds.playbackOptions(max=True, q=True)
            frameRange.append((startFrame, endFrame))
        elif self.ui.rangeSliderRB.isChecked():
            print("rangeSlider")
            startFrame = cmds.playbackOptions(ast=True, q=True)
            endFrame = cmds.playbackOptions(aet=True, q=True)
            frameRange.append((startFrame, endFrame))
        elif self.ui.customRB.isChecked():
            startFrame = self.ui.startFrameSB.value()
            endFrame = self.ui.endFrameSB.value()
            frameRange.append((startFrame, endFrame))
        elif self.ui.bookmarkRB.isChecked():
            bookmarks = self.getCheckedBookmarks()
            for bm in bookmarks:
                frameRange.append(cmds.getAttr("{}.timeRange".format(bm))[0])

        return frameRange


    def playblastData(self):
        """

        :return:
        """
        cameraList = self.getCheckedCameras()
        frameRangeList = self.getFrameRange()
        filePath = self.getPBFilePath()

        print(filePath)
        print(cameraList)
        print(frameRangeList)

        for frameRange in frameRangeList:
            for cam in cameraList:
                PlayblastCore.doBlast(camera=cam, frameRange=frameRange, )

        # vpSettings = self.getVPSettings()
        # frameRate = self.getFrameRate()

        # pbFormat = self.getExtension()

        # for camera in cameraList:
        #     PlayblastCore.doBlast()

    def eventFilter(self, source, event):
        """
        This event filter is installed on comboboxes inside the QtTable to
        prevent auto scrolling when scrolling through the QtTable.
        :param source:
        :param event:
        :return:
        """
        if (event.type() == QEvent.Wheel and
                isinstance(source, QComboBox)):
            return True
        return super(PBTool, self).eventFilter(source, event)


def getBookmarksList():
    """
    Gets all the bookmarks from maya timeline.
    :return:
    """
    bookmarkNodes = cmds.ls(type='timeSliderBookmark')
    bookmarkData = []
    for bookmarkNode in bookmarkNodes:
        bookmarkData.append((cmds.getAttr(bookmarkNode + '.name'), bookmarkNode))
    return bookmarkData


def getCameraList():
    """

    :return:
    """
    # Using listCameras
    allCams = cmds.listCameras()
    # Sorting cameras into user made cameras and non user made cameras
    userCams = []
    defaultCams = []
    for cam in allCams:
        if cmds.camera(cam, q=True, sc=True):
            defaultCams.append(cam)
        else:
            userCams.append(cam)

    sortedCams = defaultCams + userCams
    return sortedCams


def runPBTool():
    print(pbModulePath)
    pbwindow = PBTool()
    pbwindow.show()
    return pbwindow


if __name__ == "__main__":
    app = QApplication.instance()

    if not app:
        app = QApplication(sys.argv)

    window = runPBTool()
    app.exec_()
