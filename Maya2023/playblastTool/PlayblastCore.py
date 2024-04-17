import maya.cmds as cmds
import json
import os
import ffmpegUtils

# Load JSON data from file. Maya looks for the JSON file in its bin folder.
# To avoid this we provide full path when opening JSON.
path = os.path.dirname(__file__)
with open(os.path.join(path, 'viewportData.json'), 'r') as vpDataFile:
    viewport_settings_data = json.load(vpDataFile)["viewport_settings"]

playblastSettings = {
    "filename": ["playblast.mov", "File Name", str],
    "format": ["avi", "Format", str],
    "compression": ["H.264", "Compression", str],
    "width": [1920, "Width", int],
    "height": [1080, "Height", int],
    "off_screen": [False, "Render Off Screen", bool],
    "force_overwrite": [True, "Force Overwrite", bool],
}


# viewportSettings = {
#     "displayAppearance": ['smoothShaded', "Display Appearance", str,
#                           ["smoothShaded", "wireframe", "boundingBox",
#                            "flastShaded"]],
#     "displayLights": ['default', 'Display Lights', str, ['default', 'all']],
#
#     "polymeshes": [True, "Shapes", bool],
#     "grid": [True, "Grid", bool],
#     "joints": [False, "Joints", bool],
#     "nurbsCurves": [True, "Nurbs Curves", bool],
#     "nurbsSurfaces": [True, "Nurbs Surfaces", bool],
#     "manipulators": [True, "Manipulators", bool],
#     "pivots": [True, "Pivots", bool],
#     "locators": [False, "Locators", bool],
#     "displayTextures": [True, "Display Textures", bool],
#     "textures": [True, "Textures"],
#     "useDefaultMaterial": [False, "Use Default Textures", bool]
# }


# def getDefaultVPSettings():
#     defaultSettings = {}
#     for setting in viewport_settings_data:
#         defaultSettings[setting["name"]] = setting["default_value"]
#     return defaultSettings


def getSavedVPSettings():
    """
    Grabs the JSON data and simplifies it int a dictionary with name as key and
    the list of default value, data type and all possible values as the value
    pair.
    :return:
    """
    currUISettings = {}
    for setting in viewport_settings_data:
        if setting["exposed"]:
            currUISettings[setting["name"]] = [setting["default_value"],
                                               setting["data_type"],
                                               setting["allValues"]]

    return currUISettings


def createPlayblastEditor(resolution=(1920, 1080)):
    """
    Create the modelEditor and the modelEditorPanel.
    :param resolution: tuple (int) or list(int): width and height pixels
    :return: modelEditor and window
    """
    width = resolution[0]
    height = resolution[1]
    window = cmds.window(title='Playblast View', widthHeight=(width, height))
    cmds.paneLayout(configuration="single")
    # Using a default camera for now.
    modelEditor = cmds.modelEditor(camera="persp")
    cmds.showWindow(window)
    return modelEditor, window


def updateModelEditor(pbModelEditor, vpSettings):
    """
    Updates the ModelEditor with settings passed
    :type vpSettings: object
    :param pbModelEditor: The modelEditor that needs to be updated.
    :return:
    """
    # Applying all the settings to the modelEditor before doing playblast.
    cmds.modelEditor(pbModelEditor, e=True, grid=vpSettings["grid"])
    cmds.modelEditor(pbModelEditor, e=True, joints=vpSettings["joints"])
    cmds.modelEditor(pbModelEditor, e=True,
                     nurbsCurves=vpSettings["nurbsCurves"])
    cmds.modelEditor(pbModelEditor, e=True,
                     nurbsSurfaces=vpSettings["nurbsSurfaces"])
    cmds.modelEditor(pbModelEditor, e=True,
                     displayAppearance=vpSettings["displayAppearance"])

    cmds.modelEditor(pbModelEditor, e=True,
                     displayTextures=vpSettings["displayTextures"])

    cmds.modelEditor(pbModelEditor, e=True,
                     locators=vpSettings["locators"])


def createCustomHud(hudText=None):
    pass


def createPBName(cameraName, frameRange):
    """

    :return:
    """
    scene_name = cmds.file(query=True, sceneName=True, shn=True).split(".")[
                     0] or "Untitled"

    # Sanitize camera name as it can have a ton of special characters which
    # might not be allowed to use in Windows file names.

    fileName = "{0}_{1}_{2}_{3}".format(scene_name,
                                        cameraName,
                                        int(frameRange[0]),
                                        int(frameRange[1]))

    # ToDo: Sanitize file name to remove special chars
    return fileName


def filterSettings(vpSettingsUI):
    """
    Combines the UI and default JSON settings.
    :param vpSettingsUI:
    :return:
    """
    filteredSettings = {}
    for jSetting in viewport_settings_data:
        if jSetting['name'] in vpSettingsUI.keys():
            filteredSettings[jSetting['property_name']] = vpSettingsUI[
                jSetting['name']]
        else:
            filteredSettings[jSetting['property_name']] = jSetting[
                'default_value']

    return filteredSettings


def postPBCleanup(modelEditor, pbWindow, defaultHardwareSettings=None):
    """

    :param modelEditor:
    :param defaultHardwareSettings:
    :return:
    """
    cmds.deleteUI(modelEditor)
    cmds.deleteUI(pbWindow)


def createOutputPath(filePath, frameRange):
    scene_name = cmds.file(query=True, sceneName=True, shn=True).split(".")[
                     0] or "Untitled"

    outputFileName = "{0}_{1}_{2}_Combined".format(scene_name, int(frameRange[0]),
                                               int(frameRange[1]))
    outputPath = os.path.join(filePath, outputFileName)
    return outputPath


def tilePlayblasts(inputFilePaths, pbFormat, outputPath):
    """

    :param inputFilePaths:
    :param pbFormat:
    :param outputPath:
    :return:
    """
    # Find extension
    if pbFormat == 'qt':
        ext = ".mov"
    if pbFormat == 'avi':
        ext = ".avi"

    # Adding extension
    for count in range(len(inputFilePaths)):
        inputFilePaths[count] = inputFilePaths[count] + ext

    # Adding extension
    outputPath = outputPath + ext

    ffmpegUtils.stitchTogether(inputFilePaths, outputPath)


def doBlast(cameras, vpSettingsUI, filePath, format, compression,
            frameRangeList, frameRate='ntsc', playPB=True, quality=100,
            ornaments=True, offScreen=False, pbResolution=[1920, 1080],
            hud=True,
            tilePB=False):
    """
    This function does the following
    :param frameRange:
    :param pbSettings:
    :param camera:
    :param pbSettings:
    :param format:
    :return:
    """
    vpSettings = filterSettings(vpSettingsUI)
    pbModelEditor, pbWindow = createPlayblastEditor(pbResolution)
    updateModelEditor(pbModelEditor, vpSettings)

    for frameRange in frameRangeList:
        allFilePaths = []
        outputPath = createOutputPath(filePath, frameRange)
        for cam in cameras:
            fileName = createPBName(cam, frameRange)
            cmds.modelEditor(pbModelEditor, e=True, av=True, cam=cam)
            allFilePaths.append(os.path.join(filePath, fileName))
            try:
                cmds.playblast(epn=pbModelEditor,
                               filename=os.path.join(filePath, fileName),
                               format=format,
                               offScreen=offScreen,
                               quality=100,
                               percent=100,
                               compression=compression,
                               startTime=int(frameRange[0]),
                               endTime=int(frameRange[1]),
                               viewer=playPB,
                               useTraxSounds=True,
                               cc=True
                               )
            except Exception as e:
                print(e)
        if tilePB:
            tilePlayblasts(allFilePaths, format, outputPath)
    postPBCleanup(pbModelEditor, pbWindow)


