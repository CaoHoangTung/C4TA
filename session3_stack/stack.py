class Stack:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        s = ""
        for i in range(len(self.items)-1):
            s += str(self.items[i]) + " "
        if (not self.is_empty()):
            s += str(self.items[len(self.items)-1])
        return s

    def is_empty(self):
        return len(self.items) == 0

    def push(self,val):
        self.items.append(val)

    def pop(self):
        return self.items.pop()

    def clear(self):
        self.items.clear()