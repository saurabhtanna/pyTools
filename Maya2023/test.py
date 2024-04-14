import sys
import os
import importlib
myPath = r'C:\Users\saura\pyTools\Maya2023'
if myPath not in sys.path:
    sys.path.append(myPath)

from playblastTool import PBTool
importlib.reload(blast)
blast.run()