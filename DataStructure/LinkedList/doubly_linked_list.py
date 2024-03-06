class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1

        if index < self.length // 2:
            currNode = self.head
            for _ in range(index):
                currNode = currNode.next
        else:
            currNode = self.tail
            for _ in range(self.length - 1, index, -1):
                currNode = currNode.prev

        return currNode.val

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.length += 1

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            newNode = Node(val)
            currNode = self.head
            for _ in range(index):
                currNode = currNode.next
            newNode.prev = currNode.prev
            newNode.next = currNode
            currNode.prev.next = newNode
            currNode.prev = newNode
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        if index == 0:
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            currNode = self.head
            for _ in range(index):
                currNode = currNode.next
            currNode.prev.next = currNode.next
            if currNode.next:
                currNode.next.prev = currNode.prev
        self.length -= 1