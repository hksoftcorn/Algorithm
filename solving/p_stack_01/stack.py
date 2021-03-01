

class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return False if len(self.data) else True

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            return None

    def __repr__(self):
        result = '\n-----'
        for d in self.data:
            result = '\n| {} |'.format(d) + result
        return result



s = Stack()
s.push(1)
