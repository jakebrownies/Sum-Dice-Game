# the play scene functions as the main gameplay - the user selects if they want to bet on even or odd dice roll sums. After 3 rounds, player with the higher score wins

import pygame
import pygwidgets
import pyghelpers
import random
from constants import *

class ScenePlay(pyghelpers.Scene):
    def __init__(self, window):
        
        self.rollCounter = 0                        # rollCounter keeps track of which roll out of 3 we are currently on
        self.window = window
        self.playerName = "Player 1"
        self.player1Choice = None                   # initizalized to None, this instance variable holds the player's choice of EVENS or ODDS
        self.player2Choice = None                   # this assigns the computer opponent EVENS or ODDS depending on player's choice
        self.player1Score = 0                       # Scores for both players are tracked
        self.player2Score = 0
        self.rolling = False                        # this bool is used to determine when the dice are rolling to delay 1 second
        self.rolled = (1,1)                         # roll result is initialized to a tuple of 1s
        
        # all objects are initialized - includes display text, dice images that vary depending on roll, and buttons to select evens or odds and to proceed to next roll or results
        self.backgroundImage = pygwidgets.Image(window, (0,0), resource_path('BG.png'))
        self.titleText = pygwidgets.DisplayText(window, (220, 60), "Sum of Dice", fontSize=52, fontName='Georgia')
        self.instructionText = pygwidgets.DisplayText(window, (240, 180), "Select evens or odds", fontSize=26, fontName='Georgia', textColor=WHITE, justified='center')
        self.evensButton = pygwidgets.CustomButton(window, (130, 300), resource_path('eUp.png'), down=resource_path('eDown.png'), over=resource_path('eOver.png'))
        self.oddsButton = pygwidgets.CustomButton(window, (380, 300), resource_path('oUp.png'), down=resource_path('oDown.png'), over=resource_path('oOver.png'))
        self.diceRoll1 = pygwidgets.Image(window, (60, 250), resource_path('1.png'))
        self.diceRoll2 = pygwidgets.Image(window, (320, 250), resource_path('1.png'))
        self.resultNum = pygwidgets.DisplayText(window, (275, 330), "", fontSize=56, textColor=WHITE)
        self.player1 = pygwidgets.DisplayText(window, (120, 530), f"{self.playerName}: {self.player1Score}", fontSize=32)
        self.player2 = pygwidgets.DisplayText(window, (420, 530), f"Player 2: {self.player2Score}", fontSize=32)
        self.rollButton = pygwidgets.CustomButton(window, (250, 600), resource_path('rollUp.png'), down=resource_path('rollDown.png'), over=resource_path('rollOver.png'))
        self.contButton = pygwidgets.CustomButton(window, (250, 600), resource_path('contUp.png'), down=resource_path('contDown.png'), over=resource_path('contOver.png'))
        
        # several objects initially hidden 
        self.diceRoll1.hide()
        self.diceRoll2.hide()
        self.rollButton.hide()
        self.contButton.hide()


    # this method resets all the values to ensure if the game is restarted, nothing carries over. This method is called by the leave method of this scene
    def resetValues(self):
        self.rollCounter = 0
        # ensures if the text field is left blank in successive games, the playerName still appears as 'Player 1' in this scene
        self.playerName = "Player 1"
        self.player1Choice = None
        self.player2Choice = None
        self.player1Score = 0
        self.player2Score = 0
        self.rolling = False
        self.rolled = (1,1)


    # allows the scene to receive playerName input from the previous scene
    def receive(self, receiveID, data):
        if receiveID == "playerName string":
            self.playerName = data
            print(receiveID, "received:", self.playerName)
            self.player1.setValue(f"{self.playerName}: {self.player1Score}")


    def getSceneKey(self):
        return SCENE_PLAY


    # gets a random number between 1 and 6, assigns to the rolled instance variable, and returns the results for the dice objects to display
    def getRoll(self):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        self.rolled = (roll1, roll2)
        return roll1 + roll2


    # event handling method - keyPressedList included as I may implement it in the future
    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
    

    # Dice Roll ---------------------------------------------------------------------------------------------------------------------------------------
            # activates when rolling (roll button was pressed) and sets the diceRoll objects to display the appropriate dice image based on the getRoll results
            if event.type == ROLL_DELAY_EVENT and self.rolling:
                DICE_SOUND.play()
                self.rolling = False                                                        # rolling toggled

                roll1, roll2 = self.rolled                                                  # gets the two roll results from the rolled tuple from the getRoll method
                total = roll1 + roll2
                self.diceRoll1.replace(resource_path(f"{roll1}.png"))                                      # two dice images are chosen based on roll results
                self.diceRoll2.replace(resource_path(f"{roll2}.png"))
                print(f"Dice Roll: {roll1} + {roll2} = {roll1 + roll2}")                    # print of roll math for debugging
                self.diceRoll1.show()                                                       # the two dice images are shown
                self.diceRoll2.show()
                self.resultNum.setValue(f"+                        =   {total}")            # the sum is displayed
                
                # if the result is even, determines which player should get the point
                if total % 2 == 0:
                    self.instructionText.setValue("Result is even")
                    if self.player1Choice == EVENS:
                        self.player1Score += 1
                        self.player1.setValue(f"{self.playerName}: {self.player1Score}")
                    elif self.player2Choice == EVENS:
                        self.player2Score += 1
                        self.player2.setValue(f"Player 2: {self.player2Score}")
                
                # if the result is odd, determines which player should get the point
                else:
                    self.instructionText.setValue("Result is odd")
                    if self.player1Choice == ODDS:
                        self.player1Score += 1
                        self.player1.setValue(f"{self.playerName}: {self.player1Score}")
                    elif self.player2Choice == ODDS:
                        self.player2Score += 1
                        self.player2.setValue(f"Player 2: {self.player2Score}")
                
                # the roll button is shown after initial roll
                self.rollButton.show()
                
                # once the counter reaches 3, the continue button replaces roll to allow the player to proceed to results
                if self.rollCounter == 3:
                    self.rollButton.hide()
                    self.contButton.show()


    # Evens Selected ---------------------------------------------------------------------------------------------------------------------------------------
            # the user has selected evens - if the sum of the two dice rolled is even, they receive a point
            if self.evensButton.handleEvent(event) and not self.rolling:
                
                DINK_SOUND.play()

                self.player1Choice = EVENS                                      # player choices are set to constant string values
                self.player2Choice = ODDS
                
                self.rollCounter += 1                                           # roll counter is initially incremented by 1 as roll begins right after player choice
                self.titleText.setValue("Rolling...")
                print("Rolling...")
                self.instructionText.setValue(f"Roll #{self.rollCounter}")
                self.evensButton.hide()                                         # evens and odds buttons are hidden as they are not needed
                self.oddsButton.hide()
                self.getRoll()                                                  # get roll method is called to get random dice roll results

                # the timer is set to begin the 1 second delay between rolls, rolling set to True to begin the dice roll
                pygame.time.set_timer(ROLL_DELAY_EVENT, ROLL_DELAY_TIME, loops=1)
                self.rolling = True


    # Odds Selected ---------------------------------------------------------------------------------------------------------------------------------------
            # the user has selected odds - if the sum of the two dice rolled is odd, they receive a point
            if self.oddsButton.handleEvent(event) and not self.rolling:
                
                DINK_SOUND.play()

                self.player1Choice = ODDS                                       # player choices are set to constant string values
                self.player2Choice = EVENS

                self.rollCounter += 1                                           # roll counter is initially incremented by 1 as roll begins right after player choice
                self.titleText.setValue("Rolling...")
                print("Rolling...")
                self.instructionText.setValue(f"Roll #{self.rollCounter}")
                self.evensButton.hide()                                         # evens and odds buttons are hidden as they are not needed
                self.oddsButton.hide()
                self.getRoll()                                                  # get roll method is called to get random dice roll results

                # the timer is set to begin the 1 second delay between rolls, rolling set to True to begin the dice roll
                pygame.time.set_timer(ROLL_DELAY_EVENT, ROLL_DELAY_TIME, loops=1)
                self.rolling = True
            

    # Roll Button ---------------------------------------------------------------------------------------------------------------------------------------
            # roll button appears after initial roll, proceeds to the next of the 3 rolls
            if self.rollButton.handleEvent(event) and not self.rolling:
                DINK_SOUND.play()
                self.rollCounter += 1                                           # rollCounter incremented to keep track of which roll the user is on
                self.titleText.setValue("Rolling...")
                self.instructionText.setValue(f"Roll #{self.rollCounter}")      # roll # is displayed
                self.getRoll()                                                  # get roll method is called to get random dice roll results

                
                pygame.time.set_timer(ROLL_DELAY_EVENT, ROLL_DELAY_TIME, loops=1)
                self.rolling = True


    # Continue Button ---------------------------------------------------------------------------------------------------------------------------------------
            # replaces the roll button so the user knows the next press will proceed to the results scene
            if self.contButton.handleEvent(event):
                WINNER_SOUND.play()
                self.goToScene(SCENE_RESULTS)                                   # proceeds to the Results scene


    # all Play scene objects are drawn
    def draw(self):
        self.window.fill(RED)
        self.backgroundImage.draw()
        self.titleText.draw()
        self.instructionText.draw()
        self.evensButton.draw()
        self.oddsButton.draw()
        self.diceRoll1.draw()
        self.diceRoll2.draw()
        self.player1.draw()
        self.player2.draw()
        self.resultNum.draw()
        self.rollButton.draw()
        self.contButton.draw()


    # a leave method sends scores to the Results scene's receive method so it can interpret a winner
    def leave(self):
        scores = (self.player1Score, self.player2Score)
        self.send(SCENE_RESULTS, "scores", scores)
        
        # a call to the reset method ensures all play values are reset for successive games
        self.resetValues()
        
        # as objects displayed changes throughout the Play scene, all the last objects displayed must be hidden and evens and odds buttons shown again
        self.diceRoll1.hide()
        self.diceRoll2.hide()
        self.rollButton.hide()
        self.contButton.hide()
        self.evensButton.show()
        self.oddsButton.show()
        
        # DisplayText objects' values are appropriately set for successive games
        self.titleText.setValue("Sum of Dice")
        self.instructionText.setValue("Select evens or odds")
        self.resultNum.setValue("")
        self.player1.setValue(f"{self.playerName}: {self.player1Score}")
        self.player2.setValue(f"Player 2: {self.player2Score}")
        
        print("play values reset")