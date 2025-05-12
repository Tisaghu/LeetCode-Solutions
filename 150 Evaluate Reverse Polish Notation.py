class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = ['+','-','*','/']

        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                first = int(stack.pop())
                second = int(stack.pop())

                if token == '+':
                    stack.append(second + first)
                elif token == '-':
                    stack.append(second - first)
                elif token == '*':
                    stack.append(second * first)
                else:
                    #Handle division correctly
                    if second * first > 0:
                        stack.append(second // first)
                    else:
                        stack.append(-(-second // first))
        
        return int(stack[0])


test = Solution()
print(test.evalRPN(["4","3","-"]))
print(test.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
