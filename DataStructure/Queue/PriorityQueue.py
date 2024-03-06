queue = []

def enqueue(item, priority):
    queue.append((priority, item))
    queue.sort(reverse=True)

def dequeue():
    if not queue:
        return None
    return queue.pop()[1]
