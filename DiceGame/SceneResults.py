# the results scene displays the winning player name along with a tropy image and a fanfare sound. The reset button allows the user to start another game, returning to the Splash scene

import pygwidgets
import pyghelpers
from constants import *

class SceneResults(pyghelpers.Scene):
    streak = 0
    def __init__(self, window):
        
        self.window = window
        self.playerName = "Player 1"

        # objects intitialized for Results
        self.backgroundImage = pygwidgets.Image(window, (0,0), resource_path('BG.png'))
        self.titleText = pygwidgets.DisplayText(window, (260, 60), "Results:", fontSize=52, fontName='Georgia')
        self.winner = pygwidgets.DisplayText(window, (240, 150), "", fontSize= 52, textColor=WHITE)
        self.trophy = pygwidgets.Image(window, (220, 210), resource_path('trophy.png'))
        self.currentStreak = pygwidgets.DisplayText(window, (240, 550), "", fontSize=42, textColor=WHITE)
        self.restartButton = pygwidgets.CustomButton(window, (250, 600), resource_path('rUp.png'), down=resource_path('rDown.png'), over=resource_path('rOver.png'))


    # receive method receives playerName string sent from Splash scene and also the player scores from the Play scene to determine and display the winner
    # method takes receiveID as parameter to determine what kind of data is being received - either 'playerName string' or 'scores'
    def receive(self, receiveID, data):
        if receiveID == "playerName string":
            self.playerName = data
        if receiveID == "scores":
            scores = data
            print(receiveID, "received:", scores)
            if scores[0] > scores[1]:                               # checks score tuple received to determine if user or computer has higher score
                winner = self.playerName
                self.streak += 1     
            else:
                winner = "Player 2"
                self.streak = 0
            self.winner.setValue(f"{winner} WINS!")                 # Player 1's name displayed if they're the winner, Player 2 otherwise
            self.currentStreak.setValue(f"Current Streak: {self.streak}")
            


    def getSceneKey(self):
        return SCENE_RESULTS


    # event handling method - keyPressedList included as I may implement it in the future
    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.restartButton.handleEvent(event):
                DINK_SOUND.play()
                print("Restarting game...")
                self.goToScene(SCENE_SPLASH)                        # the user is returned to the Splash scene and they can either keep their name entry or change it


    # all objects for Results scene are drawn
    def draw(self):
        self.window.fill(RED)
        self.backgroundImage.draw()
        self.titleText.draw()
        self.winner.draw()
        self.trophy.draw()
        self.currentStreak.draw()
        self.restartButton.draw()


    # the leave method ensures if the text field is left blank in successive games, the playerName still appears as 'Player 1' in this scene
    def leave(self):
        self.playerName = "Player 1"
        