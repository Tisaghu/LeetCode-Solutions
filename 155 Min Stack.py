class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.minStack.pop() 

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMin(self):
        return self.minStack[-1] if self.minStack else None

test = MinStack()

instructions = ["MinStack","push","push","push","push","getMin","pop","getMin","pop","getMin","pop","getMin"]
inputs = [[],[2],[0],[3],[0],[],[],[],[],[],[],[]]

for i in range(0, len(instructions)):
    if instructions[i] == "MinStack":
        test = MinStack()
    elif instructions[i] == "push":
        test.push(inputs[i][0])
    elif instructions[i] == "pop":
        test.pop()
    elif instructions[i] == "top":
        print(test.top())
    elif instructions[i] == "getMin":
        print(test.getMin())