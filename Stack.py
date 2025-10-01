class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.stack.pop(0)

    def peek(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
s = Stack()
s.push(5)
s.push(4)
s.push(3)
s.push(2)
s.push(1)
print("Size after push:",s.size())
print("Top element:", s.peek())

print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Is empty?", s.is_empty())
print("Pop from empty:", s.pop())