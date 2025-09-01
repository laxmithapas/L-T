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

    def printlist(self, limit=20):
        
        temp = self.head
        count = 0
        while temp and count < limit:
            print(temp.data, end=" ")
            temp = temp.next
            count += 1
        print()

    def detectLoop(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print("Loop detected")
                return True
        print("No loop detected")
        return False



llist = LinkedList()


n = int(input("Enter number of nodes: "))
nodes = []
for i in range(n):
    data = int(input(f"Enter data for node {i+1}: "))
    llist.insertend(data)
    nodes.append(data)

print("\nOriginal Linked List (limited view): ", end="")
llist.printlist()


choice = input("Do you want to create a loop? (y/n): ").lower()
if choice == "y":
    pos = int(input("Enter position to link last node to (0-based index): "))
    if pos < n:
        
        last = llist.head
        while last.next:
            last = last.next
        
        loop_node = llist.head
        for _ in range(pos):
            loop_node = loop_node.next
        last.next = loop_node
        print(f"Loop created: last node points to node with data {loop_node.data}")
    else:
        print("Invalid position, no loop created.")


llist.detectLoop()
