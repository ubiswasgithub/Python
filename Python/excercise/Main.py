'''
Created on Jan 17, 2018

@author: ubiswas
'''
import os
import Unzipfile

class Main:
    def printMessage(self):
        print "Hello"
        

fileDir = os.path.dirname(os.path.realpath('__file__'))
fileDir =  os.path.abspath(os.path.join(fileDir, os.pardir))


objZip = Unzipfile.UnzipFile()
#objZip.getRenameZipFile("E:\\Personal\\courseera\\workspace\\Python\\Scorm")
objZip.getRenameZipFile(fileDir + "\\Scorm")
#objZip.getUnZipfile("E:\\Personal\\courseera\\workspace\\Python\\Scorm", "E:\\Personal\\courseera\\workspace\\Python\\unzip")
objZip.getUnZipfile(fileDir + "\\Scorm", fileDir+ "\\unzip")
#objZip.getCombinedCsvFile("E:\\Personal\\courseera\\workspace\\Python\\unzip")
objZip.getCombinedCsvFile(fileDir+ "\\unzip")




