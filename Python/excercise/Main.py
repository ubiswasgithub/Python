'''
Created on Jan 17, 2018

@author: ubiswas
'''
import Engineering
import Humanresource
import Unzipfile

class Main:
    def printMessage(self):
        print "Hello"
        


objEng = Engineering.Engineering("TEst1", "Ar1", 1200)
objEng.greetingResource()
objEng.displayResourceAddress();
objEng.displayAnualIincrementedSalary()

objHr = Humanresource.Humanresource("HR1", "Ar1", 1200)
objHr.greetingResource()
objHr.displayResourceAddress()
objHr.displayAnualIincrementedSalary()


objZip = Unzipfile.UnzipFile()
objZip.getRenameZipFile("E:\\Personal\\courseera\\workspace\\Python\\Scorm")
objZip.getUnZipfile("E:\\Personal\\courseera\\workspace\\Python\\Scorm", "E:\\Personal\\courseera\\workspace\\Python\\unzip")
objZip.getCombinedCsvFile("E:\\Personal\\courseera\\workspace\\Python\\unzip")




