class stack :
    def __init__(self):
        self.stack = []
    def isEmpty(self):
        return self.stack == []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.isEmpty():
            raise "Stack is empty"
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            raise "Stack is empty"
        return self.stack[-1]
    def size(self):
        return len(self.stack)

if __name__ == "__main__":
    s = stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())