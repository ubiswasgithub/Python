'''
Created on Jan 17, 2018

@author: ubiswas
'''
import Custom
    
    
class Humanresource:
    obj = None
    percent = 8
    def __init__(self, name, address, salary):
        self.obj = Custom.Custom(name, address, salary)
        
    def greetingResource(self):
        self.obj.displayGreetingMessage()
    def displayResourceAddress(self):
        print  self.obj.getUserAddress()
    
    def getAnualIncrementedSalary(self):
        return (self.obj.getUserSalary()*int(12)* int(Humanresource.percent))/100   + (self.obj.getUserSalary()*int(12))
    
    def displayAnualIincrementedSalary(self):
        print self.getAnualIncrementedSalary()