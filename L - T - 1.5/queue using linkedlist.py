class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Dequeue from empty queue")

    def size(self):
        return len(self.items)
    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Front from empty queue")
    def rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Rear from empty queue")
    def display(self):
        return self.items
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Front element is:", q.front())
print("Rear element is:", q.rear())
print("Queue elements are:", q.display())
print("Queue size is:", q.size())