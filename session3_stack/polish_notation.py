class PolishNotation():
    def __init__(self):
        self.stack = []
    
    def calculate(self,s):
        for c in s:
            if c.isdigit():
                self.stack.append(int(c))
            else:
                top1 = str(self.stack.pop())
                top2 = str(self.stack.pop())
                self.stack.append(eval(top2+c+top1))
        return self.stack.pop()