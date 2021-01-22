#Arjun Bhan
#Professor Chung
#COM 110 Final Project
#Due 12/17/18

"""This program is a memory game.  The user’s goal is to click on two cards and match their numbers.
After clicking on the introduction screen, the user is tasked to select a difficulty level which determines
the number of pairs that need to be matched.  Matching a pair awards 100 points; whereas, making an incorrect
match takes away 25 points.  The game ends once all cards are successfully flipped.  Once the game ends, the
user has the option to either quit the program or play again.
"""

#These lines of code import in functions from other code 
from classes import *
from random import *
from graphics import *
from buttonclass import *
from time import sleep

#This code allows for the program to call on the functions necessary to create different grids based on the amount of cards / difficulty requested.
def option(x,win):
    grid1 = Grid(x)
    win.setCoords(-3, -3, 20, 20)
    grid1.drawGrid(win)
    return grid1

#This code is a introduction function. The reason why this code is a function is just to clean the main, since the code is only used in one spot at the begining.
def intro(win):
    firstintroText= Text(Point(500,100),"Welcome to our memory game. Your goal is to click on two cards and match their numbers.")
    colsiz(firstintroText,"white",18)
    firstintroText.draw(win)
    secondintroText=Text(Point(500,150),"Matching a pair awards 100 points; whereas, making an incorrect match deducts 25.")
    colsiz(secondintroText,"white",18)
    secondintroText.draw(win)
    thirdintroText=Text(Point(500,200),"The game ends once all cards are sucessfully flipped.  Best of luck!")
    colsiz(thirdintroText,"white",18)
    thirdintroText.draw(win)
    clickintroText= Text(Point(500,300)," Click anywhere to start. Have fun!")
    colsiz(clickintroText,"white",18)
    clickintroText.draw(win)
    pt = win.getMouse()
    firstintroText.undraw()
    secondintroText.undraw()
    clickintroText.undraw()
    thirdintroText.undraw()

#This function modifies the size and color of a text object. This code was made into a function because of its reapeated usage throughout.  
def colsiz(text,col,siz):
    text.setTextColor(col)
    text.setSize(siz)

    
#The main function contains the game rules, creates the graphical window, and has other miscellaneous code.
def main():
    #These lines of code create the GUI window and change its color.
    win = GraphWin("Match Game!", 1000, 650)
    win.setBackground("#076324")
    #This code calls upon the introduction function, providing the user an explanation of how to play the game.
    intro(win)
    #This code prompts the user to select a difficulty level and creates necessary buttons.
    difchose = Text(Point(500,200),"Select the game's difficulty level")
    colsiz(difchose,"yellow",20)
    difchose.draw(win)
    easy = Button(win, Point(200,300), 200, 100, "Easy")
    medium = Button(win, Point(500,300), 200, 100, "Medium")
    hard = Button(win, Point(800,300), 200, 100, "Hard")
    exitButton = Button(win, Point(500,100), 80, 40, "Exit")
    pt = Point(0,0)
    #This code checks which difficulty was selected and creates the necessary number of cards, beginning the game.
    while not (easy.isClicked(pt) or medium.isClicked(pt) or hard.isClicked(pt)):
        pt = win.getMouse()
        if easy.isClicked(pt):
            grid = option(1,win)
            difcar=4
        elif medium.isClicked(pt):
            grid = option(2,win)
            difcar=8
        elif hard.isClicked(pt):
            grid = option(3,win)
            difcar=12
        elif exitButton.isClicked(pt):
            win.close()
    #This code sets the variables points (keeps track of points earned) and attem (keeps track of how many pairs are left to win the game)
    points=0
    attem=0
    pointswor=Text(Point(14,16), "Points:")
    colsiz(pointswor,"orange",16)
    pointswor.draw(win)
    ptext=Text(Point(16,16), points)
    colsiz(ptext,"orange",16)
    ptext.draw(win)
    escButton=Button(win, Point(16,18), 2, 1, "Exit")
    escButton.deactivate()
    #This code creates infinite clicks as long as the escButton (second exit button) is not clicked.
    while not escButton.isClicked(pt):
            
        #This code sets the variable goodpoint to False. The variable goodpoint will be used to check whether a point was a button or not.
        goodpoint=False
        #This code makes sure that if the user clicks a non button point it will not count in the code. 
        while not goodpoint:
            pt = win.getMouse()
            #This code checks which card was clicked by looping through the matrix, just as we did in Lab 12.
            for x in range(len(grid.buttonMatrix)):
                for y in range(len(grid.buttonMatrix[x])):
                    if grid.buttonMatrix[x][y].clicked(pt):
                    #This code make sure that if the point clicked by the user was a button that the code would use it.
                        goodpoint=True
                        #This code get the value of the card.
                        rank1 = grid.buttonMatrix[x][y].getRank()
                        #This code flips over the card
                        grid.buttonMatrix[x][y].flip(win)
                        #This code allows the x and y cordinates of the user selected button to be saved.
                        x1=x
                        y1=y
        if not escButton.isClicked(pt):
            #This code sets the variable goodpoint2 to False. The variable goodpoint2 will be used to check whether a point was a button or not.
            goodpoint2=False
            #This code makes sure that if the user clicks a non button point it will not count in the code. 
            while not goodpoint2:
                pt = win.getMouse()
                #This code checks which card was clicked by looping through the matrix, just as we did in Lab 12.
                for x in range(len(grid.buttonMatrix)):
                    for y in range(len(grid.buttonMatrix[x])):
                        if grid.buttonMatrix[x][y].clicked(pt):
                        #This code make sure that if the point clicked by the user was a button that the code would use it.
                            goodpoint2=True
                            #This code get the value of the card.
                            rank2 = grid.buttonMatrix[x][y].getRank()
                            #This code flips over the cards.
                            grid.buttonMatrix[x][y].flip(win)
                            #This code allows the x and y cordinates of the user selected button to be saved.
                            x2=x
                            y2=y
            #This code makes sure if the cards do not equal eachother they flip over and points get subtracted .
            if not rank2==rank1:
                sleep(.4)
                grid.buttonMatrix[x2][y2].flip(win)
                grid.buttonMatrix[x1][y1].flip(win)
                points=points-25
            #This code awards points based on successfully selected two cards with the same rank. 
            else:
                grid.buttonMatrix[x2][y2].deactivate()
                grid.buttonMatrix[x1][y1].deactivate()
                points=points+100
                attem=attem+1
                #This code makes sure that the user will not be awarded any points for selecting the same points twice.
                if x2==x1 and y2==y1:
                    grid.buttonMatrix[x1][y1].activate()
                    points=points-100
                    attem=attem-1
            #This code makes sure that the points constantly change and that they cannot be negative. 
            if points<0:
                points=0
            ptext.undraw()
            ptext=Text(Point(16,16), points)
            colsiz(ptext,"orange",16)
            ptext.draw(win)
            #This code lets the user win the game.
            if attem==difcar:
                end=("You Win!")
                wintext=Text(Point(8,16), end)
                colsiz(wintext,"gold",60)
                wintext.draw(win)
                escButton.activate()
                restart = Button(win, Point(1,18), 7, 1, "Click here to restart the program")
                while not restart.isClicked(pt) or escButton.isClicked(pt):
                    pt = win.getMouse()
                    #This code allows the main function to call upon itself when the restart button is pressed.
                    if restart.isClicked(pt):
                        win.close()
                        main()
                    elif escButton.isClicked(pt):
                        win.close()
                    
    #This code allows the exit button to properly function.
                        
main()
