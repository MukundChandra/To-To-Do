"""
Why is the code looking like absolute crap,you ask?

This is just a test module for working out the nuances
of opening files, its just that right now I don't have
any sort of unit which can display the text files by
itself, so I have to rely on Notepad and Shell to open
them for me right now.
"""

import sys
from subprocess import call
import threading
import os
def openFiles(ListOfFiles):
    for x in ListOfFiles:
        path = os.path.dirname(x)
        name = os.path.basename(x)
        S = "cd "+path+" && "+'\"'+name+'\"'
        call(S,shell=True)

def getFiles(S):
    F = open(S,"r")
    ListOfFiles = [line.rstrip('\n') for line in F]
    F.close()
    return ListOfFiles

class ToToDo(threading.Thread):
    def __init__(self, fileToOpen):
      threading.Thread.__init__(self)
      self.fileToOpen = fileToOpen
      
    def run(self):
       openFiles([self.fileToOpen])

def main():
    MainFile = "My Files\\FilesToOpen.txt"
    L = getFiles(MainFile)
    MyThreadList = []
    for x in L:
        t = ToToDo(x)
        MyThreadList.append(t)
        t.start()

    sys.exit()

main()
