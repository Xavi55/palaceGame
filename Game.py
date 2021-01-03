#server code
#handles server & game logic
#----
#playing a '10' removes the current stack out of play
#7 can be high or low
from LinkList import LinkList
class Game:
    elimPlayers=[]
    currStack=LinkList
