class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertbegg(self, d):
        new_node = Node(d)
        new_node.next = self.head
        self.head = new_node

    def insertend(self, d):
        new_node = Node(d)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def insertatany(self, d, position):
        new_node = Node(d)
        if position == 0:   # insert at head
            new_node.next = self.head
            self.head = new_node
            return
        
        temp = self.head
        for i in range(position - 1):
            if temp is None:   # position out of range
                print("Position out of range")
                return
            temp = temp.next

        if temp is None:
            print("Position out of range")
            return
        
        new_node.next = temp.next
        temp.next = new_node

    def traversal(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next

    def Delete(self):  # delete from beginning
        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.next

    def Deleteend(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None

    def Deleteatany(self, position):
        if self.head is None:
            print("List is empty")
            return
        
        if position == 0:
            self.head = self.head.next
            return
        
        temp = self.head
        for i in range(position - 1):
            if temp is None or temp.next is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp.next is None:
            print("Position out of range")
            return

        temp.next = temp.next.next

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                print("Key is found")
                return
            temp = temp.next
        print("Key is not found")

    def sort(self):
        if self.head is None:
            print("List is empty")
            return
        index = self.head
        while index:
            current = index.next
            while current:
                if index.data > current.data:
                    index.data, current.data = current.data, index.data
                current = current.next
            index = index.next

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()



llist = LinkedList()
llist.insertbegg(3)
llist.insertbegg(2)
llist.insertbegg(4)
llist.insertbegg(5)
llist.printlist()   

