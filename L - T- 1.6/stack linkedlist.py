class Node:
    def _init_(self, d):
        self.data=d
        self.next=None
class Stack():
    def _init_(self, size):
        self.size=size
        self.head=None
        self.count=0
    def push(self,d):
        newnode=Node(d)
        if self.head==None:
            self.head=newnode
            self.count+=1
        elif self.count>self.size:
            print("Stack overflow")
        else:
            newnode.next=self.head
            self.head=newnode
        self.display()
    def pop(self):
        if self.head==None:
            print("Stack underflow")
        elif self.head.next==None:
            self.head=None
            print("Stack is empty")
        else:
            self.head=self.head.next
            self.display()

    def display(self):
        if self.head==None:
            print("Stack is empty")
        else:
            temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print("")

a=Stack(3)
a.push(9)
a.push(7)
a.push(32)
a.push(23)
a.push(43)
a.pop()
a.pop()