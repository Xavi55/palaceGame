from LinkList import LinkList
class Player:
    name=''
    hand=LinkList()
    hiddenStack=LinkList()
    shownStack=LinkList()

    def __init__(self,n):
        self.name=name

    #choose 3 cards to hide
    def hide(self,c):
        self.hiddenStack.add(c)
    
    #3 cards to be shown
    def place(self,c):
        self.shownStack.add(c)

    def pickup(self):
        pass

    def play():
        pass

    def draw():
        pass    