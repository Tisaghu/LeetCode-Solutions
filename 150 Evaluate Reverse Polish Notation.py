class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                first, second = stack.pop(), stack.pop()
                stack.append(second - first)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                first, second = stack.pop(), stack.pop()
                stack.append(int(float(second) / first))
            else:
                stack.append(int(token))
        
        return stack[0]


test = Solution()
print(test.evalRPN(["4","3","-"]))
print(test.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
