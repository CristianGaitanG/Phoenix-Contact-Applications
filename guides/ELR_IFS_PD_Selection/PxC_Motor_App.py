from PIL import ImageTk, Image
import pandas as pd
import numpy as np

try:
    import Tkinter as tk
except:
    import tkinter as tk
    from tkinter import messagebox
    
from tkinter import LEFT, RIGHT

import time
from datetime import date
import os
import sys
import math

class Clock():  
    def __init__(self):
               
        self.root = tk.Tk()
        self.root.title("Process Data Validation")
        self.root.geometry('950x720+50+50')
        self.root.resizable(False,False)
        self.root.iconbitmap('logo.ico')
        self.root['background']='white'
        
        self.frame = tk.Frame(width=220, height=50, bg="white")
        self.frame.pack(side=tk.LEFT)
        self.frame.place(anchor='ne', relx=0.25, rely=0.0)
        self.img = ImageTk.PhotoImage(Image.open("pxc_ban.jpg"))
        self.labelI = tk.Label(self.frame,image = self.img,bg="white")
        self.labelI.pack()
        
        self.frame2 = tk.Frame(width=220, height=100, bg="white")
        self.frame2.pack()
        self.frame2.place(anchor='nw', relx=0.45, rely=0.015)
        self.labelT = tk.Label(self.frame2,text="Networkable Motor Starter Selection Guide", font='Helvetica 14 bold')
        self.labelT['background']='white'
        self.labelT.pack()
        self.label = tk.Label(self.frame2,text="")
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.label.pack()
        
        self.frame3 = tk.Frame(width=600, height=100, bg="white")
        self.frame3.pack()
        self.frame3.place(anchor='nw', relx=0.05, rely=0.1)
        self.label1 = tk.Label(self.frame3,text="Part Number Selection Guide", font='Helvetica 11 bold')
        self.label2 = tk.Label(self.frame3,text="The motor starters need to be networkable, or IFS - ELR-HX-IES-XX/500AC-X-IFS.", font='Helvetica 10 bold')
        #self.label3 = tk.Label(self.frame3,text="Please follow the next steps to complete the design.", font='Helvetica 10')
        self.label1['background']='white'
        self.label1.pack(anchor="w")
        self.label2['background']='white'
        self.label2.pack(anchor="w")
        #self.label3['background']='white'
        #self.label3.pack(anchor="w")
        
#-----------------------COMMUNICATION PROTOCOL----------------------------------------------------------------------------#
        self.frame4 = tk.Frame(width=300, height=100, bg="white")
        self.frame4.pack()
        self.frame4.place(anchor='ne', relx=0.35, rely=0.17)
        self.label4 = tk.Label(self.frame4,text="1. Please choose the communication protocol  ", font='Helvetica 10')
        self.label4['background']='white'
        self.label4.pack(anchor="w")

        options = [
            "Choose one option",
            "Ethernet IP",
            "PROFINET",
            "Modbus/TCP",
            "CANOpen",
            "Profibus",
        ]
        # datatype of menu text
        self.clicked = tk.StringVar()
        # initial menu text
        self.frame7 = tk.Frame(width=300, height=100, bg="white")
        self.frame7.pack()
        self.frame7.place(anchor='n', relx=0.48, rely=0.17)
        self.clicked.set( "Choose one option" )
        self.drop = tk.OptionMenu( self.frame7 , self.clicked , *options )
        self.drop.pack()
#-----------------------PROCESS DATA----------------------------------------------------------------------------#
        self.frame16 = tk.Frame(width=500, height=500, bg="white",highlightbackground="black",highlightthickness=2)
        self.frame16.pack()
        self.frame16.place(anchor='nw', relx=0.67, rely=0.1)

        self.label20 = tk.Label(self.frame16,text="Determine number of motor \n starter per communication module ", font='Helvetica 11 bold')
        self.label20['background']='white'
        self.label20.pack()
        
        self.label20 = tk.Label(self.frame16,text="Process Data Selection: ", font='Helvetica 10 bold')
        self.label20['background']='white'
        self.label20.pack()
        
        self.label21 = tk.Label(self.frame16,text="Please select at least one data for State/Device\nand Control. Those are critical for operation.", font='Helvetica 10')
        self.label21['background']='white'
        self.label21.pack()

        self.vpd1 = tk.IntVar()
        self.vpd2 = tk.IntVar()
        self.vpd3 = tk.IntVar()
        self.vpd4 = tk.IntVar()
        self.vpd5 = tk.IntVar()
        self.vpd6 = tk.IntVar()
        self.vpd7 = tk.IntVar()
        self.vpd8 = tk.IntVar()
        self.vpd9 = tk.IntVar()
        self.vpd10 = tk.IntVar()
        self.vpd11 = tk.IntVar()
        self.vpd12 = tk.IntVar()
        self.vpd13 = tk.IntVar()
        self.vpd14 = tk.IntVar()
        self.vpd15 = tk.IntVar()
        
        self.label22 = tk.Label(self.frame16,text="State/Diagnostic", font='Helvetica 9 bold')
        self.label22['background']='white'
        self.label22.pack()
        self.pd1 = tk.Checkbutton(self.frame16, text='Device State - Right/Left direction',variable=self.vpd1, onvalue=1, offvalue=0,command=self.count_data,bg="white")
        self.pd1.pack(anchor="w")
        self.pd9 = tk.Checkbutton(self.frame16, text='Channel Status - 2 words (H/L)',variable=self.vpd9, onvalue=1, offvalue=0,command=self.count_data,bg="white")
        self.pd9.pack(anchor="w")

        self.label22 = tk.Label(self.frame16,text="Control words", font='Helvetica 9 bold')
        self.label22['background']='white'
        self.label22.pack()
        self.pd13 = tk.Checkbutton(self.frame16, text='Motor Control and Reset (Switch) - F/R/M/A',variable=self.vpd13, onvalue=1, offvalue=0,command=self.count_data,bg="white")
        self.pd13.pack(anchor="w")
        self.pd15 = tk.Checkbutton(self.frame16, text='Motor Control and Reset (Button) - F/R/M/A',variable=self.vpd15, onvalue=1, offvalue=0,command=self.count_data,bg="white")
        self.pd15.pack(anchor="w")
        
        self.label22 = tk.Label(self.frame16,text="Optional Words", font='Helvetica 9 bold')
        self.label22['background']='white'
        self.label22.pack()
        self.pd2 = tk.Checkbutton(self.frame16, text='Query Nominal Current - Bits 3...0',variable=self.vpd2, onvalue=1, offvalue=0,command=self.count_data,bg="white")
        self.pd2.pack(anchor="w")
        self.pd3 = tk.Checkbutton(self.frame16, text='Largest Current (%) of three phases',variable=self.vpd3, onvalue=1, offvalue=0,command=self.count_data,bg="white")
        self.pd3.pack(anchor="w")
        self.pd4 = tk.Checkbutton(self.frame16, text='Thermal Load (%) of the motor model',variable=self.vpd4, onvalue=1, offvalue=0,command=self.count_data,bg="white")
        self.pd4.pack(anchor="w")
        self.pd5 = tk.Checkbutton(self.frame16, text='Largest Current (A) of three phases',variable=self.vpd5, onvalue=1, offvalue=0,command=self.count_data,bg="white")
        self.pd5.pack(anchor="w")
        self.pd6 = tk.Checkbutton(self.frame16, text='Phase Current L1 (%) relation In of motor',variable=self.vpd6, onvalue=1, offvalue=0,command=self.count_data,bg="white")
        self.pd6.pack(anchor="w")
        self.pd7 = tk.Checkbutton(self.frame16, text='Phase Current L2 (%) relation In of motor',variable=self.vpd7, onvalue=1, offvalue=0,command=self.count_data,bg="white")
        self.pd7.pack(anchor="w")
        self.pd8 = tk.Checkbutton(self.frame16, text='Phase Current L3 (%) relation In of motor',variable=self.vpd8, onvalue=1, offvalue=0,command=self.count_data,bg="white")
        self.pd8.pack(anchor="w")  
        self.pd10 = tk.Checkbutton(self.frame16, text='Counter Overload Trips - 2 words (H/L)',variable=self.vpd10, onvalue=1, offvalue=0,command=self.count_data,bg="white")
        self.pd10.pack(anchor="w")
        self.pd11 = tk.Checkbutton(self.frame16, text='Operating Cycling Counters - 2 words (H/L)',variable=self.vpd11, onvalue=1, offvalue=0,command=self.count_data,bg="white")
        self.pd11.pack(anchor="w")
        self.pd12 = tk.Checkbutton(self.frame16, text='Emergency Tripping Counters - 2 words (H/L)',variable=self.vpd12, onvalue=1, offvalue=0,command=self.count_data,bg="white")
        self.pd12.pack(anchor="w")
        self.pd14 = tk.Checkbutton(self.frame16, text='Set Fix Nominal Motor Current',variable=self.vpd14, onvalue=1, offvalue=0,command=self.count_data,bg="white")
        self.pd14.pack(anchor="w")

        self.label22 = tk.Label(self.frame16,text="----------------------------------------------------------------------", font='Helvetica 9 bold')
        self.label22['background']='white'
        self.label22.pack()
        self.verify = tk.Button(self.frame16,text="Verify",command=self.matrix_value)
        self.verify.pack()
        self.label22 = tk.Label(self.frame16,text="Number of Motor Starters (Devices):", font='Helvetica 9 bold')
        self.label22['background']='white'
        self.label22.pack(side=LEFT)
        self.label25 = tk.Label(self.frame16,text="", font='Helvetica 9 bold')
        self.label25['background']='white'
        self.label25.pack()
        
#-----------------------FUNCTIONS--------------------------------------------------------------------------------------#    
        self.frame5 = tk.Frame(width=300, height=100, bg="white")
        self.frame5.pack()
        self.frame5.place(anchor='ne', relx=0.347, rely=0.22)
        self.label5 = tk.Label(self.frame5,text="2. Please choose the functions of the Starter   ", font='Helvetica 10')
        self.label5['background']='white'
        self.label5.pack()

        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.frame8 = tk.Frame(width=300, height=100, bg="white")
        self.frame8.pack()
        self.frame8.place(anchor='nw', relx=0.4, rely=0.225)
        self.c1 = tk.Checkbutton(self.frame8, text='Forward',variable=self.var1, onvalue=1, offvalue=0,bg="white")
        self.c1.pack(side=LEFT)
        self.c2 = tk.Checkbutton(self.frame8, text='Reverse',variable=self.var2, onvalue=1, offvalue=0,bg="white")
        self.c2.pack(side=LEFT)
        self.c3 = tk.Checkbutton(self.frame8, text='E-Stop',variable=self.var3, onvalue=1, offvalue=0,bg="white")
        self.c3.pack(side=LEFT)

#-----------------------CURRENT MOTOR----------------------------------------------------------------------------------#
        self.frame6 = tk.Frame(width=600, height=100, bg="white")
        self.frame6.pack()
        self.frame6.place(anchor='ne', relx=0.344, rely=0.275)
        self.label6 = tk.Label(self.frame6,text="3. Please specify the current of the motor (A)  ", font='Helvetica 10')
        self.label6['background']='white'
        self.label6.pack()

        self.var5 = tk.IntVar()
        self.var6 = tk.IntVar()
        self.var7 = tk.IntVar()
        self.frame9 = tk.Frame(width=300, height=100, bg="white")
        self.frame9.pack()
        self.frame9.place(anchor='nw', relx=0.4, rely=0.275)
        self.c5 = tk.Checkbutton(self.frame9, text='0.6A',variable=self.var5, onvalue=1, offvalue=0,bg="white")
        self.c5.pack(side=LEFT)
        self.c6 = tk.Checkbutton(self.frame9, text='3.0A',variable=self.var6, onvalue=1, offvalue=0,bg="white")
        self.c6.pack(side=LEFT)
        self.c7 = tk.Checkbutton(self.frame9, text='9.0A',variable=self.var7, onvalue=1, offvalue=0,bg="white")
        self.c7.pack(side=LEFT)

#-----------------------BUTTON FIND--------------------------------------------------------------------------------------#
        self.frame10 = tk.Frame(width=600, height=100, bg="white")
        self.frame10.pack()
        self.frame10.place(anchor='ne', relx=0.333, rely=0.33)
        self.label7 = tk.Label(self.frame10,text="4. Search Part Numbers for your application ", font='Helvetica 10')
        self.label7['background']='white'
        self.label7.pack()

        self.frame11 = tk.Frame(width=300, height=100, bg="white")
        self.frame11.pack()
        self.frame11.place(anchor='nw', relx=0.4, rely=0.33)
        self.execute = tk.Button(self.frame11,text="Find",command=self.find_values)
        self.execute.pack()

#----------------------DISPLAY SOLUTION - GATEWAY----------------------------------------------------------------------#
        self.frame12 = tk.Frame(width=600, height=100, bg="white")
        self.frame12.pack()
        self.frame12.place(anchor='ne', relx=0.25, rely=0.4)
        self.label8 = tk.Label(self.frame12,text="Gateway Solution: ", font='Helvetica 10')
        self.label8['background']='white'
        self.label8.pack()

        self.frame13 = tk.Frame(width=300, height=100, bg="white")
        self.frame13.pack()
        self.frame13.place(anchor='nw', relx=0.4, rely=0.4)
        self.label8 = tk.Label(self.frame13,text="", font='Helvetica 10')
        self.label8['background']='white'
        self.label8.pack()
        
#----------------------DISPLAY SOLUTION - MOTOR------------------------------------------------------------------------#
        self.frame14 = tk.Frame(width=600, height=100, bg="white")
        self.frame14.pack()
        self.frame14.place(anchor='ne', relx=0.265, rely=0.45)
        self.label9 = tk.Label(self.frame14,text="Motor Starter alternatives: ", font='Helvetica 10')
        self.label9['background']='white'
        self.label9.pack()

        self.frame15 = tk.Frame(width=300, height=100, bg="white")
        self.frame15.pack()
        self.frame15.place(anchor='nw', relx=0.4, rely=0.45)
        self.label9 = tk.Label(self.frame15,text="", font='Helvetica 10')
        self.label9['background']='white'
        self.label9.pack()

#----------------------CONSIDERATION FOR USER------------------------------------------------------------------------#
        self.frame17 = tk.Frame(width=600, height=100, bg="white",highlightbackground="black",highlightthickness=2)
        self.frame17.pack()
        self.frame17.place(anchor='ne', relx=0.56, rely=0.55)
        self.label30 = tk.Label(self.frame17,text="Please consider the next: ", font='Helvetica 10 bold')
        self.label30['background']='white'
        self.label30.pack()

        self.label31 = tk.Label(self.frame17,text="* Proces data is a 16-bit word containing different information in each bit. For more \n information please refer to datasheet.", width=60,font='Helvetica 10')
        self.label31['background']='white'
        self.label31.pack()
        self.label31 = tk.Label(self.frame17,text="* The max. number of motor starters in one single gateway is: \n 32 units using IFS_Conf Software; \n 15 units using GDSLM (PROFINET); \n 15 units using Web Browser Manager (Ethernet).", width=60,font='Helvetica 10')
        self.label31['background']='white'
        self.label31.pack()
        self.label31 = tk.Label(self.frame17,text="* The max. number of process data per motor starter is 16.",width=60, font='Helvetica 10')
        self.label31['background']='white'
        self.label31.pack()
        self.label31 = tk.Label(self.frame17,text="* Please make sure that T-Bus is connected from gateway to the final motor \n starter. This ensures that the data is collected by gateway.", width=60,font='Helvetica 10')
        self.label31['background']='white'
        self.label31.pack()

#----------------------DEVELOPED BY------------------------------------------------------------------------#
        self.frame17 = tk.Frame(width=600, height=100, bg="white",highlightbackground="black",highlightthickness=2)
        self.frame17.pack()
        self.frame17.place(anchor='ne', relx=0.584, rely=0.875)
        self.label30 = tk.Label(self.frame17,text="For more information please visit Phoenix Contact website: www.phoenixcontact.com/en-au \n Or email us to: customerservice@phoenixcontact.com.au - Phone number: 1300 786 2116", font='Helvetica 9')
        self.label30['background']='white'
        self.label30.pack()
        self.label33 = tk.Label(self.frame17,text="Demo tool developed by: Phoenix Contact - South Australia Office / Cristian Garcia, Applications Engineer", font='Helvetica 7 bold')
        self.label33['background']='white'
        self.label33.pack()
             

        self.root.mainloop()
        
#----------------------Functions------------------------------------------------------------------------#
    def count_data(self):
        countData = self.vpd1.get()+self.vpd2.get()+self.vpd3.get()+self.vpd4.get()+self.vpd5.get()+self.vpd6.get()+self.vpd7.get()+self.vpd8.get()+(2*self.vpd9.get())+(2*self.vpd10.get())+(2*self.vpd11.get())+(2*self.vpd12.get())+self.vpd13.get()+self.vpd14.get()+self.vpd15.get()
        if countData >= 16:
            print("You have reached the max number of Process data per module")
            tk.messagebox.showinfo("ALERT","You have reached the max number of Process Data per module. \nPlease consider to add a new gateway in a different rack to \ncollect the desired information.")
            self.pd1.deselect()
            self.pd2.deselect()
            self.pd3.deselect()
            self.pd4.deselect()
            self.pd5.deselect()
            self.pd6.deselect()
            self.pd7.deselect()
            self.pd8.deselect()
            self.pd9.deselect()
            self.pd10.deselect()
            self.pd11.deselect()
            self.pd12.deselect()
            self.pd13.deselect()
            self.pd14.deselect()
            self.pd15.deselect()
    
    def matrix_value(self):
        totalData = self.vpd1.get()+self.vpd2.get()+self.vpd3.get()+self.vpd4.get()+self.vpd5.get()+self.vpd6.get()+self.vpd7.get()+self.vpd8.get()+(2*self.vpd9.get())+(2*self.vpd10.get())+(2*self.vpd11.get())+(2*self.vpd12.get())+self.vpd13.get()+self.vpd14.get()+self.vpd15.get()
        if totalData == 0:
            tk.messagebox.showinfo("ALERT","Please choose one option for the next process data. They are mandatory for calculations.")
        if totalData != 0:
            print(totalData)
            numDev = math.floor(64/ totalData)
            self.label25.configure(text=numDev)
        
        
    def find_values(self):
        dataset1 = pd.read_excel('HMS_Selection.xlsx',index_col=0,header=2,sheet_name='Gateway')
        dataset2 = pd.read_excel('HMS_Selection.xlsx',index_col=0,header=2,sheet_name='HMS')

        if self.clicked.get()=='Choose one option':
            tk.messagebox.showinfo("ALERT","Please choose one option for communication protocol. This value is mandatory.")
        #if self.clicked.get()=='Choose one option' and self.var1.get() ==0 and self.var2.get() ==0 and self.var3.get() ==0 and self.var5.get() ==0 and self.var6.get() ==0 and self.var7.get() ==0:
        #    tk.messagebox.showinfo("ALERT","Please choose one option for Communication protocol, function and current. Mandatory values.")
        if self.clicked.get()!='Choose one option' and self.var1.get() ==0 and self.var2.get() ==0 and self.var3.get() ==0 and self.var5.get() ==0 and self.var6.get() ==0 and self.var7.get() ==0:
            tk.messagebox.showinfo("ALERT","Please choose one option for motor function and motor current. Mandatory values.")
        if self.clicked.get()!='Choose one option' and (self.var1.get() !=0 or self.var2.get() !=0 or self.var3.get() !=0) and self.var5.get() ==0 and self.var6.get() ==0 and self.var7.get() ==0:
            tk.messagebox.showinfo("ALERT","Please choose one option for motor current. Mandatory value.")
        if self.clicked.get()!='Choose one option' and (self.var1.get() !=0 or self.var2.get() !=0 or self.var3.get() !=0) and (self.var5.get() !=0 or self.var6.get() !=0 or self.var7.get() !=0):
            data = dataset1[(dataset1.Protocol == self.clicked.get())]
            print(self.clicked.get())
        
            if self.var1.get() ==1 and self.var2.get() ==0 and self.var3.get() ==0:
                data1 = dataset2[(dataset2.Function1 == "Forward")&(dataset2.Function2 == "Not")&(dataset2.Function3 == "Not")&(dataset2.Function4 == "Overload")]
                if self.var5.get() == 1 and self.var6.get() == 0 and self.var7.get() == 0:
                    dataF = data1[(data1.Current ==0.6)]
                if self.var5.get() == 0 and self.var6.get() == 1 and self.var7.get() == 0:
                    dataF = data1[(data1.Current ==3)]
                if self.var5.get() == 0 and self.var6.get() == 0 and self.var7.get() == 1:
                    dataF = data1[(data1.Current ==9)]
                
            if self.var1.get() ==1 and self.var2.get() ==1 and self.var3.get() ==0:
                data1 = dataset2[(dataset2.Function1 == "Forward")&(dataset2.Function2 == "Reverse")&(dataset2.Function3 == "Not")&(dataset2.Function4 == "Overload")]
                if self.var5.get() == 1 and self.var6.get() == 0 and self.var7.get() == 0:
                    dataF = data1[(data1.Current ==0.6)]
                if self.var5.get() == 0 and self.var6.get() == 1 and self.var7.get() == 0:
                    dataF = data1[(data1.Current ==3)]
                if self.var5.get() == 0 and self.var6.get() == 0 and self.var7.get() == 1:
                    dataF = data1[(data1.Current ==9)]
            
            if self.var1.get() ==1 and self.var2.get() ==1 and self.var3.get() ==1:
                data1 = dataset2[(dataset2.Function1 == "Forward")&(dataset2.Function2 == "Reverse")&(dataset2.Function3 == "Emergency Stop")&(dataset2.Function4 == "Overload")]
                if self.var5.get() == 1 and self.var6.get() == 0 and self.var7.get() == 0:
                    dataF = data1[(data1.Current ==0.6)]
                if self.var5.get() == 0 and self.var6.get() == 1 and self.var7.get() == 0:
                    dataF = data1[(data1.Current ==3)]
                if self.var5.get() == 0 and self.var6.get() == 0 and self.var7.get() == 1:
                    dataF = data1[(data1.Current ==9)]
            
            if self.var1.get() ==1 and self.var2.get() ==0 and self.var3.get() ==1:
                data1 = dataset2[(dataset2.Function1 == "Forward")&(dataset2.Function2 == "Not")&(dataset2.Function3 == "Emergency Stop")&(dataset2.Function4 == "Overload")]
                if self.var5.get() == 1 and self.var6.get() == 0 and self.var7.get() == 0:
                    dataF = data1[(data1.Current ==0.6)]
                if self.var5.get() == 0 and self.var6.get() == 1 and self.var7.get() == 0:
                    dataF = data1[(data1.Current ==3)]
                if self.var5.get() == 0 and self.var6.get() == 0 and self.var7.get() == 1:
                    dataF = data1[(data1.Current ==9)]     
        
            test1 = str(data.iloc[0]['Part Number'])
            test2 = str(data.iloc[0]['Descriptor'])
            test3 = "-"
            now=test1+test3+test2
            self.label8.configure(text=now)
        
            row,col = dataF.shape
            text2=""
            for i in range(row):
                text2=text2+str(dataF.iloc[i]['Part Number'])+" - "+str(dataF.iloc[i]['Descriptor'])+";\n"        
                print(text2)

            self.label9.configure(text=text2)
                
        self.update_clock()

    def update_clock(self):
        today = date.today()
        now = time.strftime("%H:%M:%S")
        d1 = today.strftime("%d/%m/%Y")
        self.label.configure(text=now)
        self.root.after(600, self.update_clock)
        
app=Clock()
