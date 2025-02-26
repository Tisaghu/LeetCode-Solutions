class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = ['+','-','*','/']

        
        for token in tokens:
            #push non operators on to the stack
            if token not in operators:
                stack.append(token)
            else:
                #pop the previous 2 elements off the stack
                pop1, pop2 = int(stack[-1]), int(stack[-2])
                stack.pop()
                stack.pop()
                
                #perform operations:
                if token == '+':
                    newVal = pop1 + pop2
                elif token == '-':
                    newVal = pop1 - pop2
                elif token == '*':
                    newVal = pop1 * pop2
                elif token == '/':
                    newVal = pop2 // pop1 if pop2 * pop1 > 0 else -(-pop2 // pop1)

                #push the new value back on to the stack
                stack.append(newVal)
        return int(stack[0])


test = Solution()
print(test.evalRPN(["4","3","-"]))
print(test.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
