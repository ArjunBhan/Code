#Arjun Bhan
#Professor Chung
#COM 110 Final Project
#Due 12/17/18

"""This program contains the classes for a memory game.  The user’s goal in this game is to click on two cards
and match their numbers.  After clicking on the introduction screen, the user is tasked to select a difficulty
level which determines the number of pairs that need to be matched.  Matching a pair awards 100 points; whereas,
making an incorrect match takes away 25 points.  The game ends once all cards are successfully flipped.  Once the
game ends, the user has the option to either quit the program or play again.
"""




from random import * #import the random class
from graphics import *

class matchObject:
    #This code initializes the matchObject class
    #It sets up many of the values we will be using later in the code
    
    def __init__(self, center, width, height):
        #This code allows us to chose the placment of the cards.
        self.center = center
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        #This code begins the game with all the cards face down versus upwards.
        self.faceUp = False
        #This code sets the button as active.
        self.activate()

    def setUpVals(self,rank,suit):
        #This code sets up a variable for the rank and suit of a card. 
        self.rank = rank
        self.suit = suit
        #This code sets the card's image to that of a face down card.
        self.image = Image(self.center, "playingcards/b1fv.gif")

    def drawObj(self,win):
        # This code draws the cards in the window.
        self.image.draw(win)
    #This function is used to flip the cards.
    def flip(self, win):
        #This code sets up the faceUp variable as the card being face down and False.
        #Since the code is natrually set up as False it will start turned over
        if self.faceUp:
            self.faceUp = False
            self.image = Image(self.center, "playingcards/b1fv.gif")
            print("facedown")
        else:
            #This code modifies a card to be face up if faceUp is changed to True.
            #Since the code is naturally set up as False it will transform the image file if the code output True.
            self.faceUp = True
            self.image = Image(self.center, "playingcards/" + str(self.suit) + str(self.rank) + ".gif")
            print("faceup")
        self.image.undraw()
        self.image.draw(win)
        #This code makes sure that the new cards will be drawn and that cards do not draw ontop of eachother.

    def activate(self):
        #This function sets a boolean variable to check if a card is active. The code sets the function self.activate as True.
        self.active = True
    def deactivate(self):
        #This function sets a boolean variable to check if a card is deactive. The code sets the function self.activate as False.
        self.active = False         
    def clicked(self, p):

        #This code makes sure that, if a click happend between certain points and the button was active, it would allow the code to work.
        #If the button is not active it will not let this function happen
        if (self.xmin < p.getX() < self.xmax) and (self.ymin < p.getY() < self.ymax) and self.active:
            return True
        else:
            return False
    def getRank(self):
        #This code returns the rank of a playing card.
        return self.rank

class Grid:
    #This code sets the cordinates of each card. This code also determines how many cards will be made and what difficulty the code will be on.
    # This code also tell the program the height and width of the cards.
    def __init__(self, difficulty):       
        if difficulty == 1:
            xSize,ySize = 4,2
            total = 8
            centers = [Point(2,3),Point(6,3),Point(11,3),Point(15,3),Point(2,8),Point(6,8),Point(11,8),Point(15,8)]
            width = 1.7
            height = 3.2
        elif difficulty == 2:
            xSize,ySize = 4,4
            total = 16
            centers = [Point(2,3),Point(6,3),Point(11,3),Point(15,3),Point(2,8),Point(6,8),Point(11,8),Point(15,8),Point(2,13),Point(6,13),Point(11,13),Point(15,13),Point(18,8),Point(-1,8),Point(-1,3),Point(18,3)]
            width = 1.7
            height = 3.2
        elif difficulty == 3:
            xSize,ySize = 6,4
            total = 24
            centers = [Point(4,3),Point(8,3),Point(12,3),Point(17,3),Point(4,8),Point(8,8),Point(12,8),Point(17,8),Point(2,3),Point(6,3),Point(10,3),Point(14,3),Point(2,8),Point(6,8),Point(10,8),Point(14,8),Point(2,13),Point(6,13),Point(10,13),Point(14,13),Point(8,-1),Point(-1,8),Point(-1,3),Point(8,13)]
            width = 1.7
            height = 3.2
        self.buttonMatrix = []
        assignList = []
        centerIndex = 0
        #This code puts down a bunch of randomly sorted cards down for each point. 
        for r in range(xSize):
            row = []
            for c in range(ySize):
                matchObj = matchObject(centers[centerIndex], width, height)
                centerIndex += 1
                row.append(matchObj)
                assignList.append(matchObj)
            self.buttonMatrix.append(row)
        vals = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        #This code randomly selects a value above and makes it one of the card values
        for i in range(int(total/2)):
            index = randrange(13-i)
            cardRank = vals.pop(index)
            #This code makes sure two cards with the same rank will be drawn.  The cards will eithier be a spade or a heart.
            #Once a randomly selected value is used it will be unable to be used again because of being poped from the list.

            partner1 = assignList.pop(randrange(len(assignList)))
            partner1.setUpVals(cardRank,"h")
            partner2 = assignList.pop(randrange(len(assignList)))
            partner2.setUpVals(cardRank,"s")

    #This code will draw a card for each point listed in the buttonMatrix list.
    def drawGrid(self, win):
        for i in range(len(self.buttonMatrix)):
            for j in range(len(self.buttonMatrix[0])):
                self.buttonMatrix[i][j].drawObj(win)





