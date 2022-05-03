"""Final Project
Christina Williams
The Worm Farm
File: WormFarm.py
"""
from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font


class WormFarmWindow(EasyFrame):
   
    def __init__(self):

        """Sets up the window and the label."""
        EasyFrame.__init__(self, width = 900, height = 500, title = 'Worm Farm')
        self.addLabel(text = 'Welcome to the Worm Farm!', row = 1, column = 0)
        self.setBackground("white")

        """Add Worm Picture"""

        imageLabel= self.addLabel(text ="",row=0,column=0)
        self.image=PhotoImage(file="wormPic.GIF")
        imageLabel["image"]=self.image

        """Add label and field for food scrap input"""
        self.addLabel(text = "How many pounds of food scraps does your family have each week? (Hint- the average is 4 lbs per person.)",
        row=2,column=0)
        self.foodScrapField= self.addFloatField(value=0.0,row =2, column = 4,)

        """Command button to calculate number of worms required"""
        self.calcWormFood = self.addButton(text = "Calculate Pounds of Worms Required", row = 2,
                                        column = 4,
                                        command = self.wormFood)

        """Add label and field for worm population input"""
        self.addLabel(text = "How many pounds of worms did you start with?",
        row=4,column=0)
        self.wormPopField= self.addFloatField(value=0.0,row =4, column = 4,)

        """Command button to project worm pop in 90 days"""
        self.calcWormPop90 = self.addButton(text = "90 Day Population Projection (3 months)", row = 4,
                                        column = 2,
                                        command = self.wormPop90)
        
        """Command button to project worm pop in 180 days"""
        self.calcWormPop180 = self.addButton(text = "180 Day Population Projection (6 months)", row = 4,
                                        column = 3,
                                        command = self.wormPop180)

        """Command button to project worm pop in 1 year"""
        self.calcWormPop1yr = self.addButton(text = "1 Year Population Projection", row = 4,
                                        column = 4,
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
    WormFarmWindow().mainloop()

if __name__ == '__main__':
    main()
