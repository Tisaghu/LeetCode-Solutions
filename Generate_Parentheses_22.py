class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # only add open parenthesis if open < n
        # only add close parenthesis if close < open
        # valid IIF open == close == n

        stack = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append(''.join(stack))
                return

            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(')')
                backtrack(openN, closeN + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res




test = Solution()
print(test.generateParenthesis(3)) #["((()))","(()())","(())()","()(())","()()()"]
print(test.generateParenthesis(1)) #["()"]