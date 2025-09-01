class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insertbegg(self, d):
        new_node = Node(d)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.next = self.head
            temp.next = new_node
            self.head = new_node

    # Insert at end
    def insertend(self, d):
        new_node = Node(d)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    # Print the list
    def printlist(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()



clist = CircularLinkedList()
clist.insertend(10)
clist.insertend(20)
clist.insertbegg(5)
clist.insertend(30)

clist.printlist()   