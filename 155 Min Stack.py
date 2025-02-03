class MinStack(object):

    def __init__(self):
        #initialize stack
        self.stack = []

        #initialize min stack
        self.min_stack = []

        #initialize the min value 
        self.min = None
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        #push the element on to the stack
        self.stack.append(val)

        #update min value if necessary
        if self.min == None:
            self.min = val
            self.min_stack.append(val)
        elif val <= self.min:
            self.min = val
            self.min_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        #check if this element is the min element
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
            if len(self.min_stack) == 0:
                self.min = None
            else:
                self.min = self.min_stack[-1]

        #pop the element from the stack
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        #return the top element of the stack
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        #return the min element
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

obj = MinStack()
obj.push(0)
obj.push(1)
obj.push(0)
print(obj.getMin())
obj.pop()
print(obj.getMin())