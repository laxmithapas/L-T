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

    def middleNode(self):
        if self.head is None:
            print("List is empty")
            return None
        
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("Middle node is:", slow.data)
        return slow.data



llist = LinkedList()

n = int(input("Enter number of nodes: "))
for i in range(n):
    data = int(input(f"Enter data for node {i+1}: "))
    llist.insertend(data)

print("Linked List is:", end=" ")
llist.printlist()

llist.middleNode()

