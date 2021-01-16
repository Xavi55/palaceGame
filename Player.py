from LinkList import LinkList
class Player:
    def __init__(self,n):
        #use `self` to attach variable to this player
        #otherwise its like a static variable
        #every inst of player points to the same variable/memory
        self.name=n
        self.hand=LinkList()
        self.hiddenStack=LinkList()
        self.shownStack=LinkList()
        self.hasTurn=False

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
