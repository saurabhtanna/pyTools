import maya.cmds as cmds
import json
import os

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


def getDefaultVPSettings():
    defaultSettings = {}
    for setting in viewport_settings_data:
        defaultSettings[setting["name"]] = setting["default_value"]
    return defaultSettings


def getSavedVPSettings():
    currUISettings = {}
    for setting in viewport_settings_data:
        if setting["exposed"]:
            currUISettings[setting["name"]] = [setting["current_value"],
                                               setting["data_type"],
                                               setting["allValues"]]

    return currUISettings


def createPlayblastEditor():
    """
    :return:
    """
    width = playblastSettings["width"][0]
    height = playblastSettings["height"][0]
    window = cmds.window(title='Playblast View', widthHeight=(width, height))
    cmds.paneLayout(configuration="single")
    modelEditor = cmds.modelEditor(camera="persp")
    cmds.showWindow(window)
    return modelEditor


def updateModelEditor(pbModelEditor, vpSettings):
    """
    Updates the ModelEditor with settings passed
    :param modelEditor:
    :return:
    """
    # Applying all the settings to the modelEditor before doing playblast.
    cmds.modelEditor(pbModelEditor, e=True, grid=vpSettings["grid"][0])
    cmds.modelEditor(pbModelEditor, e=True, joints=vpSettings["joints"][0])
    cmds.modelEditor(pbModelEditor, e=True,
                     nurbsCurves=vpSettings["nurbsCurves"][0])
    cmds.modelEditor(pbModelEditor, e=True,
                     nurbsSurfaces=vpSettings["nurbsSurfaces"][0])
    cmds.modelEditor(pbModelEditor, e=True,
                     displayAppearance=vpSettings["displayAppearance"][0])

    cmds.modelEditor(pbModelEditor, e=True,
                     displayTextures=vpSettings["displayTextures"][0])

    cmds.modelEditor(pbModelEditor, e=True,
                     locators=vpSettings["locators"][0])


def createCustomHud(hudText=None):
    pass


def doBlast(camera, pbSettings, vpSettings, format, frameRange=None):
    """
    This function does the following
    :param playblastSettings:
    :param format:
    :return:
    """
    vpSettings = viewportSettings  # For Now
    pbModelEditor = createPlayblastEditor()
    updateModelEditor(pbModelEditor, vpSettings)
    cmds.modelEditor(pbModelEditor, e=True, av=True)
    # cmds.playblast(epn=pbModelEditor)
