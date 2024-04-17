import subprocess
#Todo: no hardcoding!

sharedPath = r"C:/Users/saura/pyTools/Shared/ffmpeg/bin"

def getFFMPEG():
    return r"{}/ffmpeg.exe".format(sharedPath)


def getFFPROBE():
    return r"{}/ffprobe.exe".format(sharedPath)


def getFFPLAY():
    return r"{}/ffplay.exe".format(sharedPath)



def stitchTogether(vidList, outputVid):
    """

    :param vidList:
    :return:
    """
    print(vidList, outputVid)
    ffmpegCommand = createXStackCommand(vidList, outputVid)
    executeFFMPEG(ffmpegCommand)


def executeFFMPEG(command):
    """

    :return:
    """
    print(command)
    subprocess.run(command)


def vidMatrix(numOfInput=2):
    """
    Calculate  a
    :param numOfInput:
    :return:
    """
    xCells = 2
    yCells = 2
    while numOfInput > xCells * yCells:
        if xCells <= yCells:
            xCells += 1
        else:
            yCells += 1
    return xCells, yCells


def layoutLogic(totalVids):
    """
    A painful way to make the layout for the videos. I'm sorry for this!
    :param totalVids:
    :return:
    """
    xCells, yCells = vidMatrix(totalVids)
    layoutList =[]
    complexLayout = ""

    xLayout = []
    yLayout = []

    for x in range(xCells):
        if x == 0:
            xLayout.extend(['0'])
        elif x == 1:
            xLayout.extend(["w{}".format(x - 1)])
        else:
            xLayout.extend(["{0}+w{1}".format(xLayout[-1], (x - 1))])

    for y in range(yCells):
        if y == 0:
            yLayout.extend(['0'])
        elif y == 1:
            yLayout.extend(["h{}".format(y - 1)])
        else:
            yLayout.extend(["{0}+h{1}".format(xLayout[-1], (y - 1))])

    for y in yLayout:
        for x in xLayout:
            layoutList.extend(["{}_{}|".format(x, y)])

    # We dont need all of them. Even though we might have a 4x4 matrix,
    # if we have only 3 videos we need only 3 layout bits
    for vidCount in range(totalVids):
        complexLayout += layoutList[vidCount]

    complexLayout = complexLayout[:-1]

    return complexLayout

def createXStackCommand(inputFiles, outputFile):
    """
    This function creates ffmpeg command for xStack filter.
    :param inputFiles:
    :param outputFile:
    :param layout:
    :return:
    """

    ffmpeg = getFFMPEG()
    vidCount = len(inputFiles)
    matrixSize = vidMatrix(vidCount)

    command = [ffmpeg]

    # Add input files
    for input_file in inputFiles:
        command.extend(['-i', input_file])

    # Add filter_complex option
    command.extend(['-filter_complex'])

    # Create filter string
    complexFilter = ""
    for i in range(vidCount):
        complexFilter += (('[{0}:v] setpts=PTS-STARTPTS, '
                          'scale=2560/{2}:1440/{3} [a{1}];')
                          .format(i, i, vidCount, vidCount))

    # Create layout logic
    vidLayout = ""
    for i in range(vidCount):
        vidLayout += "[a{}]".format(i)

    vidLayout = ("{0}xstack=inputs={1}:layout={2}:fill=black[out]".
                 format(vidLayout, vidCount, layoutLogic(vidCount)))
    command.extend([complexFilter + vidLayout])

    # Add mapping for the output
    command.extend(['-map', '[out]'])

    # Add output file
    command.append(outputFile)

    return command


# myCommand = ['C:/Users/saura/pyTools/Shared/ffmpeg/bin/ffmpeg.exe',
#              '-i', 'C:/temp/DefaultPlayblast/test1_persp_1_150.mov',
#              '-i', 'C:/temp/DefaultPlayblast/test1_front_1_150.mov',
#              '-filter_complex',
#              '[0:v] setpts=PTS-STARTPTS, scale=1920/2:1080/2 [a0]; [1:v] setpts=PTS-STARTPTS, scale=1920/2:1080/2 [a1];'
#              '[a0][a1]xstack=inputs=2:layout=0_0|w0_0:fill=black[out]',
#              '-map', '[out]', 'C:/temp/DefaultPlayblast/combined2.mov']

# inputFiles = ['C:/temp/DefaultPlayblast/test1_persp_1_150.mov',
#               'C:/temp/DefaultPlayblast/test1_front_1_150.mov']
# outputFile = 'C:/temp/DefaultPlayblast/combined2.mov'
# stitchTogether(inputFiles, outputFile)
