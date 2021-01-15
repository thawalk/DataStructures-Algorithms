# Time Complexity of every method = O(1) | Space Complexity of every method = O(1)

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
        newMinMax = {"min": number, "max": number}
        if len(self.minMaxStack):
            lastMin = self.minMaxStack[-1]['min']
            lastMax = self.minMaxStack[-1]['max']
            newMinMax["min"] = min(lastMin, number)
            newMinMax['max'] = max(lastMax, number)
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)
        # Don't do below because getting min and max of list is not O(1) operation
        # self.stack.append(number)
        # newMin = min(self.stack)
        # newMax = max(self.stack)
        # self.minMaxStack.append({"min":newMin, "max":newMax})


    def getMin(self):
        return self.minMaxStack[-1]["min"]

    def getMax(self):
        return self.minMaxStack[-1]["max"]

