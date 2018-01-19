'''
Created on Jan 18, 2018

@author: ubiswas
'''
import zipfile

import os, fnmatch

class UnzipFile:
    
    def getUnZipfile(self, filepath, destination):
        listOfFiles = os.listdir(filepath)
        pattern = "*.zip"
        counter = 0
        for filename in listOfFiles:
            if fnmatch.fnmatch(filename, pattern):
                zip_ref = zipfile.ZipFile(filepath+"\\"+filename,"r")
                zipdata = zip_ref.namelist()
                zip_ref.extractall(destination) 
                for z in zipdata:
                    for csvfile in os.listdir(destination):                        
                        if z == csvfile:
                            try:
                                os.rename(destination+"\\"+csvfile, destination + "\\"+csvfile.split(".")[0]+"_"+str(counter)+".csv")
                            except:
                                print "file not found"                               
                                            
            counter = counter +1                       
        zip_ref.close()
        print "All Zips are extracted successfully to "+ destination
        
    def getCombinedCsvFile(self,destination):        
        listoffiles = os.listdir(destination)
        fout = open(destination+"\\"+"combined.csv", 'a')
        for csv in listoffiles:
            for line in open(destination +"\\"+csv):
                fout.write(line)
        fout.close()
        print "Combined multiple CSV files to one"
        
        
    def getRenameZipFile(self, source):
        print source
        listOfFiles = os.listdir(source)
        pattern = "*.zip"
        
        for filename in listOfFiles:
            if fnmatch.fnmatch(filename, pattern):
                filepart = filename.split(".")
                fileparts = filepart[0].split("_")
                datepart = fileparts[2]
                date = datepart[0:2]
                month = datepart[2:4]
                year = datepart[4:]
                
                renameString = fileparts[0]+ "_" + fileparts[1] + " " + year +" "+ month + " "+ date
                try:
                    os.rename(source+"\\"+filename, source + "\\"+renameString+".zip")
                except:
                    print "file not found"
                    
        print "All Zip files are renamed"
                
            
