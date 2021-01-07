class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkList:
    def __init__(self):
        self.head=None
        self.length=0
    
    def add(self,val):
        new=Node(val)
        if self.isEmpty():
            self.head=new
            self.length+=1
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=new
            self.length+=1
    
    #zero indexed linkList
    def removeAt(self,idx):
        if not self.isEmpty() and idx>=0:
            if idx is 0:
                temp=self.head.val
                self.length=0
                self.head=None
            else:
                curr=self.head
                prev=None
                count=0
                while curr!=None:
                    if(idx is count):
                        temp=curr.val
                        prev.next=curr.next
                        self.length-=1
                        return temp
                    else:
                        count+=1
                        prev=curr
                        curr=curr.next
        return -1            
    
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
        if not self.isEmpty():
            curr=self.head
            while curr!=None:
                if curr.val is self.head.val:
                    print(curr.val,'head')
                else:
                    print(curr.val)
                curr=curr.next
        return -1
    
    def removeTail(self):
        if not self.isEmpty():
            s=self.length
            if s is 1:
                temp=self.head.val
                self.head=None
                return temp
            else:
                return self.removeAt(self.length-1)
    
    def isEmpty(self):
        if self.head is None and self.length is 0:
            return True
        return False

'''
l=LinkList()
l.add(1)
l.add(2)
l.add(3)
l.removeAt(2)
l.removeAt(1)
l.removeAt(0)
#l.swap(2,0)
'''