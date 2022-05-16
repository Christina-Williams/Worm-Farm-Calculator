"""Final Project
Christina Williams
The Worm Farm
File: WormFarm.py
"""
 
from tkinter import *
from breezypythongui import *
from breezypythongui import EasyMenubutton
from tkinter import PhotoImage


FoodScraps=0

class MainWindow(EasyFrame):
    
    def __init__(self):

        """Sets up the window and the label."""

        EasyFrame.__init__(self, width = 900, height = 500, title = 'The Worm Farm')
        self.addLabel(text = '', row = 1, column = 0)
        self.setBackground("white")

        "Adds the introduction label"

        self.addLabel(text = "Welcome to The Worm Farm!",
        row=2,columnspan = 1,column=0)

        "Adds the user manual button and opens it in a new window"

        self.UserManual = self.addButton(text = "Help", row = 2,
                                        column = 7,
                                        columnspan = 1,
                                        command= UserManualWindow)
        
        """Adds Header Image"""

        imageLabel= self.addLabel(text ="",row=1,column=0,columnspan = 30,)
        self.image=PhotoImage(file="FoodScraps.GIF")
        imageLabel["image"]=self.image

        """Add worm food text area to the window (in __init__)"""

        self.outputArea = self.addTextArea("Vermicomposting refers to the natural process of decomposing organic materials with the help of composting worms. The Red Wiggler worm is great for composting because of their insatiable appetite. Use the calculator below to find out how many pounds of worms you can feed with your household food scraps.", 
        wrap=WORD,row = 4, column = 0,columnspan = 20, width = 5, height = 1)

        
        """Add label and field for food scrap input"""

        self.addLabel(text = "Pounds of food scraps per week (AVG is 4 lbs per person) :",
        row=5,columnspan = 1,column=0)
        self.foodScrapField= self.addFloatField(value=0.0,row =5, column = 5,)

        """Command button to calculate number of worms required"""

        self.calcWormFood = self.addButton(text = "Calculate Food", row = 6,
                                        column = 3,
                                        columnspan = 1,
                                        command= self.wormFood) 

        """Add text area for population calculator (in __init__)"""

        self.outputArea = self.addTextArea("Red Wiggler worms rapidly reproduce. Enter the amount of worms you've purchased below. Calculate your worm population in 90 days, 180 days and 1 year.", wrap=WORD,row = 7, column = 0,
                                    columnspan = 20,
                                    width = 5, height = 1,)
    
        """Add label and field for worm population input"""

        self.addLabel(text = "Pounds of worms purchased: ",
        row=8,column=0)
        self.wormPopField= self.addFloatField(value=0.0,row =8, column = 5)

        """Command button to project worm pop in 90 days"""

        self.calcWormPop90 = self.addButton(text = "90 Day Projection", row = 9,
                                        column = 2,
                                        columnspan = 1,
                                        command = self.wormPop90)
        
        """Command button to project worm pop in 180 days"""

        self.calcWormPop180 = self.addButton(text = "180 Day Projection ", row = 9,
                                        column = 3,
                                        columnspan = 1,
                                        command = self.wormPop180)

        """Command button to project worm pop in 1 year"""

        self.calcWormPop1yr = self.addButton(text = "1 Year Projection", row = 9,
                                        column = 4,
                                        columnspan = 1,
                                        command = self.wormPop1yr)

       
    """Function to calc the pound of worms required"""

    def wormFood(self):
        "clears existing error messages"
        self.addLabel(text = "                                                                                                  ",
            row=3,column=3, background="white", foreground="white")
        
        while True:   
            try:
                FoodScraps=self.foodScrapField.getNumber()
            except ValueError:
                errorMessage=self.addLabel(text = "Error - Enter a number and try again",
                row=3,column=3, background="Red", foreground="white")
            else:
                numWorms=FoodScraps / 3.5
                self.foodScrapField.setNumber(round(numWorms,1))
            break

            
    """Function to calc the projected worm population in 90 days"""

    def wormPop90(self):

        "clears existing error messages"
        self.addLabel(text = "                                                                                                  ",
            row=3,column=3, background="white", foreground="white")
        
        while True:   
            try:
                wormPop=self.wormPopField.getNumber()
            except ValueError:
                errorMessage=self.addLabel(text = "Error - Enter a number and try again",
                row=3,column=3, background="Red", foreground="white")
            else:
                numWorms=wormPop * 1.5
                self.wormPopField.setNumber(numWorms)
            break
        
    """Function to calc the projected worm population in 180 days"""

    def wormPop180(self):
        "Clears existing error messages"

        self.addLabel(text = "                                                                                                  ",
            row=3,column=3, background="white", foreground="white")
        
        while True:   
            try:
                wormPop=self.wormPopField.getNumber()
            except ValueError:
                errorMessage=self.addLabel(text = "Error - Enter a number and try again",
                row=3,column=3, background="Red", foreground="white")
            else:
                numWorms=wormPop * 3
                self.wormPopField.setNumber(numWorms)
            break
        
    
    """Function to calc the projected worm population in 1 year"""

    def wormPop1yr(self):
        
        "Clears existing error messages"

        self.addLabel(text = "                                                                                                  ",
            row=3,column=3, background="white", foreground="white")
        
        while True:   
            try:
                wormPop=self.wormPopField.getNumber()
            except ValueError:
                errorMessage=self.addLabel(text = "Error - Enter a number and try again",
                row=3,column=3, background="Red", foreground="white")
            else:
                numWorms=wormPop * 6
                self.wormPopField.setNumber(numWorms)
            break

class UserManualWindow(EasyFrame):
    
    def __init__(self):

        """Sets up the window and the labels for user manual window."""

        EasyFrame.__init__(self, width = 900, height = 500, title = 'The Worm Farm')
        self.addLabel(text = 'User Manual', row = 1, column = 0)
        self.setBackground("#D3D3D3")

        """Sets up the text area for the user manual window.""" 
        self.outputArea = self.addTextArea("GENERAL INFORMATION - The Worm Farm is an easy to use calculator for worm farmers. Use it to caluculate how many worms you can feed with your food scraps and how your population grows over time.                                                                                                                                        CALCULATE FOOD - To calculate how many worms you can feed with your food scraps, enter the pounds of food scraps you have weekly. Don't include things like meat, cheese and greasy foods because worms won't eat them. This number is just an estimate and will change from week to week.                                                                                                                                                    WORM POPULATION CALCULATOR- Find out how many worms youll have over time with the population calculator. Enter the amount of worms you purchased and project the population in 90 days, 180 and 1 year.", wrap=WORD,row = 2, column = 0,
                                    columnspan = 20,
                                    width = 5, height = 1)

        "Adds the close button to the user manual window"
        self.closeWin = self.addButton(text = "Close", row = 4,
                                        column = 0,
                                        columnspan = 20,
                                        command= self.destroy)
        
def main():

    """Instantiates and pops up the window."""

MainWindow().mainloop()

if __name__ == '__main__':
    main()
