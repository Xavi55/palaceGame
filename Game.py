#server code
#handles server & game logic
#----
#playing a '10' removes the current stack out of play
#7 can be high or low
from LinkList import LinkList
from Player import Player
from Deck import Deck
class Game:
    self.eliminatedPlayers=[]
    self.removedCards=[]
    self.currentStack=LinkList()

    def startGame():
        #how many players? -- 2-4?
        pass

