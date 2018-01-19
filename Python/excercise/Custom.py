'''
Created on Jan 17, 2018

@author: ubiswas
'''

class Custom:
    
    def __init__(self, name, address, salary):
        self.name = name
        self.address = address
        self.salary = salary
        
    def displayGreetingMessage(self):
        print "Hello "+ self.name
    def getUserName(self):
        return self.name
    def getUserAddress(self):
        return self.address
    def getUserSalary(self):
        return int(self.salary)
    
