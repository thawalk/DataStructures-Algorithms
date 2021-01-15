class MinMaxStack:
    def __init__(self):
        self.minMaxStack = []
        self.stack = []

    def peek(self):
        return self.stack[-1]
    
    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        self.stack.append(number)
        newMin = min(stack)
        newMax = max(stack)
        self.minMaxStack.append({"min":newMin, "max":newMax})


    def getMin(self):
        return self.minMaxStack[-1]["min"]

    def getMax(self):
        return self.minMaxStack[-1]["max"]

