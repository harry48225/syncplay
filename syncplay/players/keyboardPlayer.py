from syncplay import constants
from syncplay.players.basePlayer import BasePlayer
import keyboard

class KeyboardPlayer(BasePlayer):
    speedSupported = False
    customOpenDialog = False
    chatOSDSupported = False
    alertOSDSupported = False
    osdMessageSeparator = ";"

    def __init__(self, client):
        from twisted.internet import reactor
        self.reactor = reactor
        self._client = client
        self._paused = False
        self.reactor.callFromThread(self._client.initPlayer, self)
        print("init keyboard player")
        self.reactor.callFromThread(self._client.updateFile, "owo.mov", 69, "/home/shokushu/videos/homework")

        keyboard.add_hotkey(164, self.togglePaused)
    
    def setPaused(self, value):
        # Toggle the playing state
        #keyboard.send('play/pause')
        if (value != self._paused):
            self._paused = not self._paused
            keyboard.send(164)

    def togglePaused(self):
        self._paused = not self._paused
        print(f"toggled pause to {self._paused}")
    
    def setPosition(self, value):
        pass
    
    def askForStatus(self):
        self._client.updatePlayerStatus(self._paused, self._client.getGlobalPosition())

    def displayMessage(self, message, duration=..., secondaryOSD=False, mood=...):
        pass

    def setFeatures(self, featureList):
        pass

    def openFile(self, filePath, resetPosition=False):
        pass

    @staticmethod 
    def run(client, playerPath, filePath, args):
        print("running keyboard player")
        return KeyboardPlayer(client)

    @staticmethod
    def getDefaultPlayerPathsList():
        return []
    @staticmethod
    def isValidPlayerPath(path):
        return "keyboard" in path.lower()

    @staticmethod
    def getIconPath(path):
        return None

    @staticmethod
    def getExpandedPath(path):
        return path

    @staticmethod
    def getPlayerPathErrors(playerPath, filePath):
        return None

    # def _getFilename(self):
    #     self._getProperty('filename')

    # def _getLength(self):
    #     self._getProperty('length')

    # def _getFilepath(self):
    #     self._getProperty('path')
