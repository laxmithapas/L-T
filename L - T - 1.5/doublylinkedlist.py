class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_begin(self, data):
        new_node = Node(data)
        if self.head is None:  # empty list
            self.head = new_node
        else:
            new_node.next = self.head   # link new node to old head
            self.head.prev = new_node   # old head prev → new node
            self.head = new_node        # update head

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:   # empty list
            self.head = new_node
            return
        temp = self.head
        while temp.next:   # go to last node
            temp = temp.next
        temp.next = new_node   # last node next → new node
        new_node.prev = temp   # new node prev → last node

    # Display list forward
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")
dll = DoublyLinkedList()
dll.insert_begin(10)
dll.insert_end(20)
dll.insert_begin(5)
dll.insert_end(30)

dll.display()
