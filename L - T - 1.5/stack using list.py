class stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
    def display(self):
        return self.stack
s = stack()
s.push(10)  
s.push(20)
s.push(30)
print("Top element is:", s.peek())
print("Stack elements are:", s.display())
print("Stack size is:", s.size())

