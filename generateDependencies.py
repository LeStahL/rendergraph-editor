#!/usr/bin/env python
from PyQt5 import uic
import argparse, os.path

def checkPresent(dir):
    if not os.path.isfile(dir):
        raise argparse.ArgumentError('Specified file ' + dir + ' does not exist.')
    return dir

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Dependency generator script for rendergraph-editor")
    parser.add_argument('--ui', help='Supply an Qt ui file to convert to a python module.', type=checkPresent, dest='uiFile')

    args, rest = parser.parse_known_args()

    if args.uiFile != None:
        pyFileName = args.uiFile.replace('.ui', '.py').replace('\\', '/')
        pyFileNameComponents = pyFileName.split('/')
        pyFileNameComponents[-1] = "ui_" + pyFileNameComponents[-1]
        pyFileName = "/".join(pyFileNameComponents)
        print('Compiling ui file ' + args.uiFile + ' to ' + pyFileName + ' ...')
        pyFile = open(pyFileName, "wt")
        if not pyFile.writable():
            print("Error: Could not write to " + pyFileName)
            quit()
        uic.compileUi(args.uiFile, pyFile)
        print('Done.')
