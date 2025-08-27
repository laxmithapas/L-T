class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self):
        
        self.head = None
    
    def is_empty(self):
        
        return self.head is None
    
    def insert_at_beginning(self, data):
        
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def insert_at_position(self, data, position):
        
        if position < 1:
            print("Error: Position must be a positive integer")
            return
        
        if position == 1:
            self.insert_at_beginning(data)
            return
        
        new_node = Node(data)
        current = self.head
        count = 1
        
        
        while current and count < position - 1:
            current = current.next
            count += 1
        
        if current is None:
            print(f"Error: Position {position} is out of bounds")
            return
        
        new_node.next = current.next
        current.next = new_node
    
    def delete_from_beginning(self):
        if self.is_empty():
            print("Error: List is empty")
            return None
        
        deleted_data = self.head.data
        self.head = self.head.next
        return deleted_data
    
    def delete_from_end(self):
        
        if self.is_empty():
            print("Error: List is empty")
            return None
        
        if self.head.next is None:
            # Only one node in the list
            deleted_data = self.head.data
            self.head = None
            return deleted_data
        
        current = self.head
        while current.next.next:
            current = current.next
        
        deleted_data = current.next.data
        current.next = None
        return deleted_data
    
    def delete_from_position(self, position):
        if self.is_empty():
            print("Error: List is empty")
            return None
        
        if position < 1:
            print("Error: Position must be a positive integer")
            return None
        
        if position == 1:
            return self.delete_from_beginning()
        
        current = self.head
        count = 1
        
        
        while current and count < position - 1:
            current = current.next
            count += 1
        
        if current is None or current.next is None:
            print(f"Error: Position {position} is out of bounds")
            return None
        
        deleted_data = current.next.data
        current.next = current.next.next
        return deleted_data
    
    def search(self, data):
        
        current = self.head
        position = 1
        
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        
        return -1  
    
    def length(self):
        
        count = 0
        current = self.head
        
        while current:
            count += 1
            current = current.next
        
        return count
    
    def traverse(self):
        
        if self.is_empty():
            print("List is empty")
            return
        
        current = self.head
        elements = []
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print(" -> ".join(elements))
    
    def reverse(self):
        
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev



if __name__ == "__main__":
    
    ll = LinkedList()
    
    # Test insertion methods
    ll.insert_at_end(10)
    ll.insert_at_beginning(5)
    ll.insert_at_end(20)
    ll.insert_at_position(15, 2)
    
    print("Linked List after insertions:")
    ll.traverse()  
    
    
    print(f"Length of list: {ll.length()}")
    print(f"Search for 15: Position {ll.search(15)}")
    print(f"Search for 100: Position {ll.search(100)}")
    
    
    print(f"Deleted from beginning: {ll.delete_from_beginning()}")
    print(f"Deleted from end: {ll.delete_from_end()}")
    
    print("Linked List after deletions:")
    ll.traverse()  
    
    
    ll.reverse()
    print("Linked List after reversal:")
    ll.traverse()  