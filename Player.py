from LinkList import LinkList
class Player:
    self.name=''
    self.hand=LinkList()
    self.hiddenStack=LinkList()
    self.shownStack=LinkList()
    self.hasTurn=False
    self.turnRank=None

    def __init__(self,n):
        self.name=name

    #choose 3 cards to hide
    def hide(self,c):
        self.hiddenStack.add(c)
    
    #3 cards to be shown
    def place(self,c):
        self.shownStack.add(c)

    def pickup(self,stack):
        for i in stack:
            self.hand.add(i)

    def play(self,card):
        return self.hand.removeAt(card)
