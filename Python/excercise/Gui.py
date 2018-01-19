'''
Created on Jan 18, 2018

@author: ubiswas
'''

from Tkinter import *

class App:
    def __init__(self,master):
        self.var = IntVar()
        master.minsize(width=666, height=666)
        frame = Frame(master)
        frame.grid()
        f2 = Frame(master)
        f2.grid(row=0,column=1)       
        button = Checkbutton(frame,text='show',variable=self.var,command=self.fx)
        button.grid(row=0,column=0)
        msg2="""I feel bound to give them full satisfaction on this point"""
        self.v= Message(f2,text=msg2)
        
        
        f3 = Frame(master)
        f3.grid(row=0,column=1)       
        button = Checkbutton(frame,text='show',variable=self.var,command=self.fx)
        button.grid(row=1,column=0)
        msg3="""Hello"""
        self.v= Message(f3,text=msg3)


    def fx(self):
        if self.var.get():
            self.v.grid(column=1,row=0,sticky=N)
        else:
            self.v.grid_remove()

top = Tk()
top.resizable(width=False, height=False)
app = App(top)           
top.mainloop()
