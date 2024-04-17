import inspect
import os
import sys

# Get the directory of the currently executing script
pbModulePath = os.path.dirname(inspect.getfile(inspect.currentframe()))

# Add the directory to sys.path if not already in there
if pbModulePath not in sys.path:
    sys.path.append(pbModulePath)

import maya.cmds as cmds
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog,
                             QTableWidgetItem, QComboBox,
                             QCheckBox, QAbstractItemView, QMessageBox)
from PyQt5.QtCore import Qt, QEvent
import PlayblastCore
import ui_playblast
import importlib

# ToDO: Remove this when done!!!!
importlib.reload(ui_playblast)
importlib.reload(PlayblastCore)


class PBTool(QMainWindow):

    def __init__(self):
        super(PBTool, self).__init__()

        self.ui = ui_playblast.Ui_MainWindow()
        self.ui.setupUi(self)

        # Get Default and Saved UI values from VP JSON file
        self.savedVPSettings = PlayblastCore.getSavedVPSettings()

        # Setup UI
        self.ui.settingsTableWidget.verticalHeader().setVisible(False)
        self.ui.browseButton.clicked.connect(self.browseFiles)
        self.ui.savePathTextEdit.setText("C:/temp/DefaultPlayblast")
        self.populateSettingsTable()
        self.refreshCameraCombobox()
        self.refreshBookmarkComboBox()
        self.radioButtonToggleWidgets()
        self.ui.hdQuality.setChecked(True)
        self.ui.fps30RB.setChecked(True)
        self.ui.aviRB.setChecked(True)
        self.ui.timeSliderRB.setChecked(True)

        # Setup Connections
        self.ui.refreshCamerasButton.clicked.connect(
            self.refreshCameraCombobox)
        self.ui.bookmarkRefreshButton.clicked.connect(
            self.refreshBookmarkComboBox)
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
        :return: pbFilePath
        """
        pbFilePath = self.ui.savePathTextEdit.toPlainText()
        return pbFilePath

    def populateSettingsTable(self, vpSettings=None):
        """
        Populate the settings table using the
        :param vpSettings: dict: dictionary obtained from viewportData.json
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
                    toggleItem = QCheckBox("Toggle")
                    vpTable.setCellWidget(rowPosition, 1, toggleItem)
                    toggleItem.setChecked(self.savedVPSettings[settingName][0])
                if self.savedVPSettings[settingName][1] == 'list':
                    selectValue = QComboBox()
                    selectValue.installEventFilter(self)
                    selectValue.addItems(self.savedVPSettings[settingName][2])
                    vpTable.setCellWidget(rowPosition, 1, selectValue)
                    selectValue.setCurrentText(self.savedVPSettings[settingName][0])

        vpTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        vpTable.setSelectionMode(QAbstractItemView.NoSelection)

    def radioButtonToggleWidgets(self):
        """
        Handle enable and disabling of certain widgets based on respective
        radioButtons being checked in the UI.
        :return: None
        """
        self.ui.bookmarkComboBox.setEnabled(self.ui.bookmarkRB.isChecked())
        self.ui.bookmarkRefreshButton.setEnabled(
            self.ui.bookmarkRB.isChecked())
        self.ui.startFrameSB.setEnabled(self.ui.customRB.isChecked())
        self.ui.endFrameSB.setEnabled(self.ui.customRB.isChecked())

    def refreshCameraCombobox(self):
        """
        Clears and re-adds camera list to the combobox. Can help when cameras
        are added or removed to the scene. Also checks the default cameras.
        :return: None
        """
        self.ui.cameraComboBox.clear()
        camList = getCameraList()
        for cam in camList:
            self.ui.cameraComboBox.addItem(cam)
            # ToDo: Add a way to remember checked cameras before refreshing and
        #  then check them again in the comboBox.
        #  This way we can remember user selections pre-refresh.
        self.ui.cameraComboBox.checkItem('persp')

    def refreshBookmarkComboBox(self):
        """
        Refreshes the contents of bookmark combobox.
        :return: None
        """
        self.ui.bookmarkComboBox.clear()
        bookmarks = getBookmarksList()
        for bookmark in bookmarks:
            frameRange = cmds.getAttr(bookmark[1] + ".timeRange")
            itemString = "{0} {1}".format(bookmark[0], frameRange[0])
            self.ui.bookmarkComboBox.addItem(itemString, bookmark[1])

    def getCheckedCameras(self):
        """
        Returns the list of checked camera names in the cameraComboBox
        :return: list(str): List of camera names.
        """
        camList = self.ui.cameraComboBox.getCheckedItems()
        return camList

    def getCheckedBookmarks(self):
        """
        Returns the list of checked Bookmarks maya object name from
        bookmarkComboBox
        :return: bmList:
        """
        bmList = self.ui.bookmarkComboBox.getCheckedData()
        return bmList

    def getFrameRange(self):
        """
        Checks the frame range mode and finds the range based on the mode.
        :return: tuple: Tuple of start and end frame.
        """
        frameRange = []
        if self.ui.timeSliderRB.isChecked():
            startFrame = cmds.playbackOptions(min=True, q=True)
            endFrame = cmds.playbackOptions(max=True, q=True)
            frameRange.append((startFrame, endFrame))
        elif self.ui.rangeSliderRB.isChecked():
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

    def getFrameRate(self):
        """
        Check the frameRate radiobutton selection and based on the selection
        returns the appropriate keyword corresponding to the fps.
        :return: str : Frame Rate keyword based on the fps selection.
        """
        if self.ui.fps30RB.isChecked():
            return "ntsc"
        if self.ui.fps60RB.isChecked():
            return "ntscf"

    def getFormat(self):
        """
        Grabs the extension from the UI based on radiobutton selection.
        :return: str: extension.
        """
        if self.ui.aviRB.isChecked():
            return "avi", "IYUV codec"
        if self.ui.movRB.isChecked():
            return "qt", "H.264"
        if self.ui.pngRB.isChecled():
            return "qt", "png"

    def getResolution(self):
        """
        Checks UI for the selected Resolution and returns a list of
        height and width pixels.
        :return: list[int]: resolution
        """
        if self.ui.lowQuality.isChecked():
            return [640, 480]
        if self.ui.hdQuality.isChecked():
            return [1280, 720]
        if self.ui.fhdQuality.isChecked():
            return [1920, 1080]

    def getVPSettings(self):
        """
        Reads settings name and values from the settingsTableWidget.
        And returns it as a key value pair.
        :return: dict: Name Value pair dict.
        """
        tableData = {}
        vpTable = self.ui.settingsTableWidget
        for rowPos in range(vpTable.rowCount()):
            if isinstance(vpTable.cellWidget(rowPos, 1), QCheckBox):
                tableData[vpTable.item(rowPos, 0).text()] = vpTable.cellWidget(
                    rowPos, 1).isChecked()
            if isinstance(vpTable.cellWidget(rowPos, 1), QComboBox):
                tableData[vpTable.item(rowPos, 0).text()] = vpTable.cellWidget(
                    rowPos, 1).currentText()
        return tableData

    def getExtraSettings(self):
        """

        :return:
        """
        showOrnaments = self.ui.ornamentsCheckBox.isChecked()
        offScreen = self.ui.offScreenCheckBox.isChecked()
        openPB = self.ui.openPBCheckBox.isChecked()

        return showOrnaments, offScreen, openPB

    def playblastData(self):
        """

        :return:
        """
        cameraList = self.getCheckedCameras()
        frameRangeList = self.getFrameRange()
        filePath = self.getPBFilePath()
        frameRate = self.getFrameRate()
        pbFormat, compression = self.getFormat()
        pbResolution = self.getResolution()
        vpSettingsUI = self.getVPSettings()

        showOrnaments, offScreenPB, openPB = self.getExtraSettings()

        combineBlasts = self.ui.stitchCheckBox.isChecked()

        # Tile playblast can only work when multiple cameras are selected.
        if combineBlasts:
            if len(cameraList) <= 1:
                msg = "Please select multiple cameras to use this feature."
                popUpMsgWindow("Error!", msg)
                return

        PlayblastCore.doBlast(cameras=cameraList,
                              frameRangeList=frameRangeList,
                              filePath=filePath,
                              pbResolution=pbResolution,
                              format=pbFormat,
                              compression=compression,
                              quality=100,
                              playPB=openPB,
                              offScreen=offScreenPB,
                              ornaments=showOrnaments,
                              hud=True,
                              vpSettingsUI=vpSettingsUI,
                              tilePB=combineBlasts,
                              frameRate=frameRate,
                              )

    def eventFilter(self, source, event):
        """
        This event filter is installed on ComboBoxes inside the QtTable to
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
        bookmarkData.append(
            (cmds.getAttr(bookmarkNode + '.name'), bookmarkNode))
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


def popUpMsgWindow(title="Warning!", message="bleh!"):
    """
    When called pops up a QMessageBox with the given title and message.
    :param title: str.
    :param message: str.
    :return: None
    """
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(title)
    msg.setInformativeText(message)
    msg.setWindowTitle(title)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


def runPBTool():
    pbWindow = PBTool()
    pbWindow.show()
    return pbWindow


if __name__ == "__main__":
    app = QApplication.instance()

    if not app:
        app = QApplication(sys.argv)
    window = runPBTool()
    app.exec_()
