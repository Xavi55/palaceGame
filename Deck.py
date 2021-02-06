from random import randint
from LinkList import LinkList
class Deck:
    suits=['S','D','C','H']
    numbers=['a','2','3','4','5','6','7','8','9','10','j','q','k']
    deck=LinkList()
    def __init__(self):
        ##new deck order
        for a in self.suits:
            for b in self.numbers:
                self.deck.add(b+a)
                #self.deck.append(b+a)
        
    def shuffle(self):
        for i in range(0,51):
            random= randint(i+1,51)
            self.deck.swap(i,random)
    
    def swap(self,a,b):
        temp=self.deck[a]
        self.deck[a]=self.deck[b]
        self.deck[b]=temp

    def show(self):
        self.deck.show()

    def draw(self):
        return self.deck.removeHead()
'''
a=Deck()
a.shuffle()
a.show()
print('tail',a.draw())
'''