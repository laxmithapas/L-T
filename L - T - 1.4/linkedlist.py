class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertbegg(self, d):
        new_node = Node(d)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

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
