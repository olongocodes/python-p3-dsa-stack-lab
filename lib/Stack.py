class Stack:

    def __init__(self, items=None, limit=100):
        self.items = items if items is not None else []
        self.limit = limit

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.limit is None or len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise OverflowError("Stack is full")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def full(self):
        return self.limit is not None and len(self.items) == self.limit

    def search(self, target):
        try:
            return len(self.items) - self.items[::-1].index(target) - 1
        except ValueError:
            return -1
