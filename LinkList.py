class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add(self,val):
        new=Node(val)
        if self.isEmpty():
            self.head=new
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=new
    
    #zero indexed linkList
    def remove(self,idx):
        if self.isEmpty() or idx<0:
            return -1
        
        if idx is 0:
            temp=self.head.val
            self.head=self.head.next
            return temp

        else:
            curr=self.head
            prev=None
            temp=None
            count=0
            while curr!=None:
                if count is idx:
                    temp=curr.val
                    prev.next=curr.next
                    return temp
                
                prev=curr
                curr=curr.next
                count+=1
    
    def swap(self,a,b):
        curr=self.head
        count=0
        nodeA=None
        nodeB=None
        foundA=False
        foundB=False
        while curr!=None:
            if count is a or count is b:
                if not foundA:
                    nodeA=curr
                    foundA=True
                elif not foundB:
                    nodeB=curr
                    foundB=True 
            count+=1
            curr=curr.next

        if foundA and foundB:
            temp=nodeA.val
            nodeA.val=nodeB.val
            nodeB.val=temp
            return 1
        #print('err')
        return -1
        
    
    def show(self):
        curr=self.head
        while curr!=None:
            print(curr.val)
            curr=curr.next
    
    def isEmpty(self):
        if self.head is None:
            return True
        return False
'''
l=LinkList()
l.add(1)
l.add(2)
l.add(3)
l.swap(2,10)
#l.remove(1)
l.show()
'''
