class Queue:

    def __init__(self):
        self.queue = []

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)
