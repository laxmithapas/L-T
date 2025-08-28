class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertbegg(self, d):
        new_node = Node(d)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def insertend(self, d):
        new_node = Node(d)
        if self.head == None:
            self.head = new_node
        else:
            Last = self.head
            while Last.next != None:
                Last = Last.next
            Last.next = new_node
    def insertatany(self, d, position):
        new_node = Node(d)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            for i in range(position - 1):
                temp = temp.next
    def traversal(self):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next
    def Delete(self):
        if self.head == None:
            print("List is empty")
        elif self.head.next == None:
            self.head = None
        else:
            self.head = self.head.next
    
        

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next



llist = LinkedList()
llist.insertbegg(3)
llist.insertbegg(2)
llist.insertbegg(4)
llist.insertbegg(5)
llist.printlist()
