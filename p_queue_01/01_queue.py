class Queue:

    def __init__(self):
        self.data = []

    def enqueue(self, x):
        self.data.append(x)

    def dequeue(self):
        self.is_empty()
        self.data.pop(0)

    def is_empty(self):
        return not bool(len(self.data))

    def get_front(self):
        return self.data[0]

    def get_rear(self):
        return self.data[-1]

    def __repr__(self):
        return self.data


q = Queue()
q.enqueue(1)  # None, q.data => [1]
q.enqueue(2)  # None, q.data => [1, 2]
q.get_front()  # 1
q.get_rear()   # 2
q.dequeue()   # 1, q.data => [2]
q.dequeue()   # 2, q.data => []