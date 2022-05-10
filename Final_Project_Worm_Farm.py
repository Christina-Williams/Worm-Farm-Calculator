"""Final Project
Christina Williams
The Worm Farm
File: WormFarm.py
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk
from breezypythongui import *
from breezypythongui import EasyMenubutton
from tkinter import PhotoImage



class MainWindow(EasyFrame):
    
    def __init__(self):

        """Sets up the window and the label."""

        EasyFrame.__init__(self, width = 900, height = 500, title = 'The Worm Farm')
        self.addLabel(text = '', row = 1, column = 0)
        self.setBackground("white")

        """Adds Header Image"""

        imageLabel= self.addLabel(text ="",row=1,column=0,columnspan = 20,)
        self.image=PhotoImage(file="header.GIF")
        imageLabel["image"]=self.image

        """Add the text area to the window (in __init__)"""

        self.outputArea = self.addTextArea("Welcome to the Worm Farm! Vermicomposting refers to the natural process of decomposing organic materials with the help of composting worms. The Red Wiggler worm is famous for composting because they can eat their body weight in food every day. Use the calculator below to find out how many pounds of worms you can feed with your household food scraps.", wrap=WORD,row = 2, column = 0,
                                    columnspan = 20,
                                    width = 5, height = 1)
        

        """Add label and field for food scrap input"""

        self.addLabel(text = "Pounds of food scraps per week (AVG is 4 lbs per person) :",
        row=3,columnspan = 20,column=0)
        self.foodScrapField= self.addFloatField(value=0.0,row =3, column = 5,)

        """Command button to calculate number of worms required"""

        self.calcWormFood = self.addButton(text = "Calculate Food", row = 4,
                                        column = 5,
                                        columnspan = 5,
                                        command= self.wormFood)

        """Add the text area for population calculator to the window (in __init__)"""

        self.outputArea = self.addTextArea("Red Wiggler worms can double their population every 90 days! Use the calculator below to find out how many worms you will have after 90 days, 180 days and 1 year.", wrap=WORD,row = 5, column = 0,
                                    columnspan = 20,
                                    width = 5, height = 1)
    
        """Add label and field for worm population input"""

        self.addLabel(text = "Pounds of worms purchased: ",
        row=6,column=0)
        self.wormPopField= self.addFloatField(value=0.0,row =6, column = 5,)

        """Command button to project worm pop in 90 days"""

        self.calcWormPop90 = self.addButton(text = "90 Day Projection", row = 7,
                                        column = 2,
                                        columnspan = 1,
                                        command = self.wormPop90)
        
        """Command button to project worm pop in 180 days"""

        self.calcWormPop180 = self.addButton(text = "180 Day Projection ", row = 7,
                                        column = 3,
                                        columnspan = 1,
                                        command = self.wormPop180)

        """Command button to project worm pop in 1 year"""

        self.calcWormPop1yr = self.addButton(text = "1 Year Projection", row = 7,
                                        column = 4,
                                        columnspan = 1,
                                        command = self.wormPop1yr)

        """Function to calc the pound of worms required"""

    def wormFood(self):
        FoodScraps=self.foodScrapField.getNumber()
        numWorms=FoodScraps / 3.5
        self.foodScrapField.setNumber(numWorms)

        
    """Function to calc the projected worm population in 90 days"""

    def wormPop90(self):
        wormPop=self.wormPopField.getNumber()
        numWorms=wormPop * 1.5
        self.wormPopField.setNumber(numWorms)
    
    """Function to calc the projected worm population in 180 days"""

    def wormPop180(self):
        wormPop=self.wormPopField.getNumber()
        numWorms=wormPop * 3
        self.wormPopField.setNumber(numWorms)
    
    """Function to calc the projected worm population in 1 year"""

    def wormPop1yr(self):
        wormPop=self.wormPopField.getNumber()
        numWorms=wormPop * 6
        self.wormPopField.setNumber(numWorms)


def main():

    """Instantiates and pops up the window."""

MainWindow().mainloop()

if __name__ == '__main__':
    main()
