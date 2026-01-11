# the splash scene functions as title screen prior to starting the game, in which user can enter a name into a text field

import pygwidgets
import pyghelpers
from constants import *

class SceneSplash(pyghelpers.Scene):
    def __init__(self, window):

        # playerName is initialized to Player 1 here so that, if no name is entered, it defaults to this
        self.window = window
        self.playerName = "Player 1"

        # all objects are initialized
        self.backgroundImage = pygwidgets.Image(window, (0,0), resource_path('BG.png'))
        self.titleText = pygwidgets.DisplayText(window, (220, 60), "Sum of Dice", fontSize=52, fontName='Georgia')
        self.diceImage = pygwidgets.Image(window, (150, 200), resource_path('Dice.png'))
        self.enterName = pygwidgets.DisplayText(window, (270, 450), "Enter Player Name:", fontSize=26)
        self.nameEntry = pygwidgets.InputText(window, (250, 480))
        self.errorText = pygwidgets.DisplayText(window, (200, 520), "", fontSize=24, textColor=WHITE)
        self.startButton = pygwidgets.CustomButton(window, (250, 600), resource_path('Up.png'), down=resource_path('Down.png'), over=resource_path('Over.png'))


    def getSceneKey(self):
        return SCENE_SPLASH
    

    # event handling method - keyPressedList included as I may implement it in the future
    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            # the text field doesn't need to do anything if user presses enter, value only used when START button is clicked
            if self.nameEntry.handleEvent(event):
                None
            if self.startButton.handleEvent(event):
                DINK_SOUND.play()
                # the playerName is assigned from the value typed into the text field
                nameEntry = str(self.nameEntry.getValue().strip())
                self.playerName = nameEntry[0:16]
                # if something was entered, it is sent to the other two scenes as they will be using the playerName as well
                if self.playerName:
                    print(self.playerName)
                    # send methods send the name entry to the receive methods of SCENE_PLAY and SCENE_RESULTS
                    self.send(SCENE_PLAY, "playerName string", self.playerName)
                    self.send(SCENE_RESULTS, "playerName string", self.playerName)
                    # the next scene is proceeded to so the game can begin
                    self.goToScene(SCENE_PLAY)
                # if the user doesn't enter anything, we just proceed to the next scene and 'Player 1' will remain the playerName
                else:
                    self.goToScene(SCENE_PLAY)


    # all objects for the scene are drawn
    def draw(self):
        self.window.fill(RED)
        self.backgroundImage.draw()
        self.titleText.draw()
        self.diceImage.draw()
        self.enterName.draw()
        self.nameEntry.draw()
        self.errorText.draw()
        self.startButton.draw()


    # the leave method ensures if the text field is left blank in successive games, the playerName still defaults to 'Player 1'
    def leave(self):
        self.playerName = "Player 1"
