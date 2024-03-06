
class queue:
    def __init__(self):
        self.queues = []
    def isEmpty(self):
        return self.queues == []
    def enqueue(self, value):
        self.queues.append(value)
    def dequeue(self):
        if self.isEmpty():
            raise "Queue is empty"
        return self.queues.pop(0)

if __name__ == "__main__":
    q = queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())