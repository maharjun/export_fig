#!/usr/bin/env python3.5

import os
from RepoManagement.BasicUtils import changedDir, getFrameDir


def SetupExportFig():

    # get Current Script Directory
    CurrentScriptDir = getFrameDir()

    # Initialize relevant directories
    BuildDir = os.path.join(os.getcwd(), 'ExportFig_build')

    # Create Path File
    if not os.path.isdir(BuildDir):
        os.mkdir(BuildDir)
    with changedDir(BuildDir):
        with open(os.path.join(BuildDir, 'ModulePath.txt')) as ModulePathFile:
            ModulePathFile.write(CurrentScriptDir)

    return True


if __name__ == "__main__":
    SetupExportFig()
