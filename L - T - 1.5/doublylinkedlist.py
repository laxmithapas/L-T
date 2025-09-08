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
    def insert_any(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp:
            if temp.data == data:
                print("Duplicate value found")
                return
            temp = temp.next
        # If no duplicates found, insert at end
        self.insert_end(data)

    def delete_begin(self):
        if self.head is None:
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
    def delete_end(self):
        if self.head is None:
            return
        if self.head.next is None:  # only one element
            self.head = None
            return
        temp = self.head
        while temp.next:  # go to last node
            temp = temp.next
        temp.prev.next = None  # unlink last node
    def delete_any(self, key):
        if self.head is None:
            return
        # If head needs to be removed
        if self.head.data == key:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return
        temp = self.head
        while temp:
            if temp.data == key:
                temp.prev.next = temp.next
                if temp.next is not None:
                    temp.next.prev = temp.prev
                return
            temp = temp.next
        print("None")
dll = DoublyLinkedList()
dll.insert_begin(10)
dll.insert_end(20)
dll.insert_begin(5)
dll.insert_end(30)

dll.display()
