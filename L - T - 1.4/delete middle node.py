class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertend(self, d):
        new_node = Node(d)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def Deleteatany(self, position):
        if self.head is None:
            print("List is empty")
            return
        
        if position == 0:  # delete head
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

    def deletemiddle(self):
        
        temp = self.head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        
        if length == 0:
            print("List is empty")
            return
        
        middle = length // 2   
        self.Deleteatany(middle)
        print(f"Deleted middle node at position {middle}")



llist = LinkedList()


n = int(input("Enter number of nodes: "))
for i in range(n):
    data = int(input(f"Enter data for node {i+1}: "))
    llist.insertend(data)

print("Original Linked List:", end=" ")
llist.printlist()


llist.deletemiddle()

print("After deleting middle node:", end=" ")
llist.printlist()
