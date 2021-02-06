#server code
#handles server & game logic
#----
#playing a '10' removes the current stack out of play
#7 can be high or low'
#first player to empty their hand,reserve and hidden cards wins
from LinkList import LinkList
from Player import Player
from Deck import Deck
from collections import OrderedDict
values={
    'j':11,
    'q':12,
    'k':13,
    'a':14
}
class Game:
    def __init__(self):
        self.eliminatedPlayers=[]##check if eliminated, check if p1.hasTurn
        self.removedCards=[]
        self.currentStack=LinkList()
        self.players=[]#arranged by card rank
        self.deck=None
        self.currTurn=0

    def addPlayer(self,p):
        #how many players? -- 2-4?
        #add players in as they join the server
        self.players.append(Player(p))

    def start(self):
        self.deck=Deck()
        self.deck.shuffle()

        #deal out 9 cards to each player
        for p in self.players:
            count=0
            while count < 9:
                if count <= 2:
                    p.hiddenStack.add(self.deck.draw())
                else:
                    p.hand.add(self.deck.draw())
                count+=1
        

        self.players[0].shownStack.add(self.players[0].hand.removeHead())
        self.players[0].shownStack.add(self.players[0].hand.removeHead())
        self.players[0].shownStack.add(self.players[0].hand.removeHead())

        self.players[1].shownStack.add(self.players[1].hand.removeHead())
        self.players[1].shownStack.add(self.players[1].hand.removeHead())
        self.players[1].shownStack.add(self.players[1].hand.removeHead())

        #determine and order players with the lowest card ASC
        #self.sortPlayers()

    def sortPlayers(self):
        newOrder={}
        for i in self.players:
            mini='aS'
            curr=i.hand.head
            while curr != None:
                if Game.getValue(curr.val) < Game.getValue(mini):
                    mini=curr.val
                curr=curr.next
            newOrder[Game.getValue(mini)]=i
        print(newOrder)
        self.players = list(newOrder.values())
        print(self.players)
        self.players[0].hand.show()
        print()
        self.players[1].hand.show()
            #i.hand.show()

    def rotateTurn(self):
        pass
        #if self.currTurn is 3:
            #self.currTurn=0

    @staticmethod
    def getValue(card):
        val=0
        if len(card) is 3:
            val=int(card[:2])
        else:
            try:
                val=int(card[0])
            except Exception:
                val=values[card[0]]
        return val

    def calcCards(prevCard,card):
        print('static')
        ##returns true from following these rules::
            #if the card played is higher than the previous card
            #if fourOfAKind
            #if a '10' was played
            #if card is a 7
            #if a seven was previously played

        #if prevCard.val

g=Game()
g.addPlayer('k')
g.addPlayer('b')
g.start()

#Game.calcCards(1,2)
