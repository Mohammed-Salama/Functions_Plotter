import tkinter as tk
import numpy as np
from tkinter import ttk
import tkinter.font as font
import matplotlib 
import matplotlib.pyplot as plt
from tkinter.messagebox import showinfo
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
#define an App class that inherits from the tk.Tk

test = 0
class FunctionPlotter(tk.Tk):
    def __init__(self):
        """
        constructor of the FunctionPlotter class
        """
        super().__init__()
        self.designWindow()
    def designWindow(self):
        """
        this function is responsible for drawing the beginnig window
        """
        WIDGET_WIDTH = 80
        LabelsFont = font.Font(family='Helvetica', size=14, weight='bold')
        ButtonsFont = font.Font(family='Helvetica', size=14)
        self.geometry('900x750')
        self.config(bg= '#8397F0')
        self.title('Functions Plotter')
        self.fx=tk.StringVar()
        self.min_x=tk.StringVar()
        self.max_x=tk.StringVar()
        tk.Label(self, text='f(x): ',font=LabelsFont,fg='#0D1B5B',bg = '#8397F0').grid(column=1 , row = 1,pady=10 , padx = 25)
        ttk.Entry(self,width=WIDGET_WIDTH,textvariable = self.fx).grid(column=2  ,row=1)    
        tk.Label(self, text='Minimum value of x : ',font=LabelsFont ,fg='#0D1B5B',bg = '#8397F0').grid(column=1  ,row=2,pady=10,padx = 25)
        ttk.Entry(self,width=WIDGET_WIDTH,textvariable = self.min_x).grid(column=2  ,row=2)
        tk.Label(self, text='Miximum value of x : ',font=LabelsFont , fg='#0D1B5B',bg = '#8397F0').grid(column=1  ,row=3,pady=10,padx = 25)
        ttk.Entry(self,width=WIDGET_WIDTH,textvariable = self.max_x).grid(column=2  ,row=3)
        if test == 1 :
            self.Test()
        tk.Button(self, text="Plot The Function", command=self.onPlotButtonPress ,bg = '#10206B',fg = 'white', font=ButtonsFont ).grid(column= 2, row= 4,pady=10)
        tk.Button(self, text="Plot New Function", command=self.onClearButtonPress ,bg = '#10206B',fg = 'white' , font=ButtonsFont ).grid(column= 2, row= 5,pady=10)
    def onPlotButtonPress(self):
        """
        Event handler of the plotting button
        """
        fx , min_x , max_x = self.getInputs()
        check , _ = self.checkInputsValidity(fx,min_x,max_x)
        if check==True:
            self.Plot(fx , min_x , max_x)
        else:
            return

    def onClearButtonPress(self):
        """
        Event handler of the clear button
        """
        self.clearInputs()
        self.Plot(0,0,0,clear=1)


    def showMessage(self,messageTitle,messageContent):
        """
        This function shows message on the screen
        """
        showinfo(title=messageTitle, message=messageContent)

    def getInputs(self):
        """
        This function takes the input from input fields
        """
        fx = self.fx.get()
        min_x= self.min_x.get()
        max_x= self.max_x.get()
        return fx , min_x , max_x
        
    def checkInputsValidity(self , fx , min_x , max_x , testc=0):
        """
        This function checks the input validity
        """
        if self.isNumber(min_x) == False:
            self.showMessage("error" , "minimum value of x must be a number")
            return False , 1
        
        if self.isNumber(max_x) == False:
            self.showMessage("error" , "maximum value of x must be a number")
            return False , 2

        if float(min_x)>= float(max_x):
              self.showMessage("error" , "Enter a valid range (max > min)")
              return False , 3
        if testc==1:
            nfx = fx
            try:
                nfx = nfx.replace('^' ,'**' )
                ny = eval(nfx)
            except:
                self.showMessage("error" , "Enter a valid function")
                return False , 4
        
        return True , 1

    def isNumber(self,str):
        try:
            float(str)
            return True
        except ValueError:
            return False

    def clearInputs(self):
        self.fx.set("")
        self.min_x.set("")
        self.max_x.set("")

    def Plot(self,fx , min_x , max_x,clear = 0):
        """
        This function is responsible for plotting the function
        """
        figure = Figure(figsize=(6, 4), dpi=100)
        figure_canvas = FigureCanvasTkAgg(figure, self)
        toolbar_frame = tk.Frame(self)
        toolbar_frame.grid(row=6,column=2,pady=10) 
        toolbar = NavigationToolbar2Tk( figure_canvas, toolbar_frame )
        axes = figure.add_subplot()
        axes.set_xlabel('x')
        axes.set_ylabel('f(x)')
        axes.set_title('Plotting f(x)')
        axes.grid()
        if clear == 0:
            x = np.linspace(float(min_x), float(max_x))
            try:
                fx = fx.replace('^' ,'**' )
                y = eval(fx)
            except:
                self.showMessage("error" , "Enter a valid function")
                return
        else:
            x=[]
            y=[]
        axes.plot(x,y)
        figure_canvas.get_tk_widget().grid(row=7,column=2,pady=10)
    def Test(self):
        self.fx.set("2 * x")
        self.min_x.set("20")
        self.max_x.set("10")
        fx , min_x , max_x = self.getInputs()
        _,err = self.checkInputsValidity(fx , min_x , max_x)
        if (err == 3):
            print("Test 1 Passed")
        else:
            print("Test 1 Failed")
            return
        
        self.fx.set("2 * x")
        self.min_x.set("salama")
        self.max_x.set("10")
        fx , min_x , max_x = self.getInputs()
        _,err = self.checkInputsValidity(fx , min_x , max_x)
        if (err == 1):
            print("Test 2 Passed")
        else:
            print("Test 2 Failed")
            return
        
        self.fx.set("2 * x")
        self.min_x.set("20")
        self.max_x.set("salama")
        fx , min_x , max_x = self.getInputs()
        _,err = self.checkInputsValidity(fx , min_x , max_x)
        if (err == 2):
            print("Test 3 Passed")
        else:
            print("Test 3 Failed")
            return
        
        self.fx.set("salama")
        self.min_x.set("20")
        self.max_x.set("30")
        fx , min_x , max_x = self.getInputs()
        _,err = self.checkInputsValidity(fx , min_x , max_x,testc=1)
        if (err == 4):
            print("Test 4 Passed")
        else:
            print("Test 4 Failed")
            return
        print("ALL TESTS PASSED SUCCESSFULLY")
        


if __name__ == "__main__":
    functionPlotter = FunctionPlotter()
    functionPlotter.mainloop()



