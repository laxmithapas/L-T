class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class StackUsingLinkedList:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            popped_node = self.top
            self.top = self.top.next
            return popped_node.data
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            return "Stack is empty"

    def is_empty(self):
        return self.top is None

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count

    def display(self):
        elements = []
        current = self.top
        while current:
            elements.append(current.data)
            current = current.next
        return elements
s = StackUsingLinkedList()
s.push(10)
s.push(20)
s.push(30)
print("Top element is:", s.peek())
print("Stack elements are:", s.display())
print("Stack size is:", s.size())
