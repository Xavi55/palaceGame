#server code
#handles server & game logic
#----
#playing a '10' removes the current stack out of play
#7 can be high or low'
#first player to empty their hand,reserve and hidden cards wins
from LinkList import LinkList
from Player import Player
from Deck import Deck
class Game:
    def __init__(self):
        self.eliminatedPlayers=[]##check if eliminated, check if p1.hasTurn
        self.removedCards=[]
        self.currentStack=LinkList()
        self.players=[]#arranged by card rank
        self.d=None

    def addPlayer(self,p):
        #how many players? -- 2-4?
        #add players in as they join the server
        self.players.append(Player(p))

    def start(self):
        self.d=Deck()
        self.d.shuffle()

        #deal out 9 cards to each player
        for p in self.players:
            count=0
            while count < 9:
                if count <= 2:
                    p.hiddenStack.add(self.d.draw())
                else:
                    p.hand.add(self.d.draw())
                count+=1

        #determine and order players with the lowest card ASC
        for i in self.players:
            i.hand.show()

    def rotateTurn(self):
        pass

    @staticmethod
    def calcCards(prevCard,card):
        pass
        #check if the card played is higher than the previous card
        #check if fourOfAKind
        #check if a '10' was played
        #check if card is a 7
        #check if a seven was previously played

        #if prevCard.val

'''
g=Game()
a=Game()
g.addPlayer('k')
g.addPlayer('b')
g.start()
'''