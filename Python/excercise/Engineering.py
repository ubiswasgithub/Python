'''
Created on Jan 17, 2018

@author: ubiswas
'''
import Custom
    
    
class Engineering:
    obj = None
    percent = 12
    def __init__(self, name, address, salary):
        self.obj = Custom.Custom(name, address, salary)
        
    def greetingResource(self):
        self.obj.displayGreetingMessage()
        
        
    def displayResourceAddress(self):
        print  self.obj.getUserAddress()
        
    def getAnualIncrementedSalary(self):
        return (self.obj.getUserSalary()*int(12)* int(Engineering.percent))/100   + (self.obj.getUserSalary()*int(12))
    
    def displayAnualIincrementedSalary(self):
        print "Your yearly Incremented salary: " 
        print self.getAnualIncrementedSalary()