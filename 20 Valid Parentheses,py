class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #create a stack to keep track of the open brackets
        stack = []

        #create a dictionary to keep track of the matching brackets
        brackets = {')':'(', '}':'{', ']':'['}

        #iterate through the string
        for char in s:
            #if the character is an open bracket, add it to the stack
            if char in brackets.values():
                stack.append(char)
            #if the character is a close bracket, check if it matches the last open bracket
            elif char in brackets.keys():
                #if the stack is empty, return False
                if not stack:
                    return False
                #if the last open bracket does not match the close bracket, return False
                if stack[-1] != brackets[char]:
                    return False
                #if the last open bracket matches the close bracket, pop it from the stack
                stack.pop()
        return not stack

test = Solution()
print(test.isValid("()")) #True
print(test.isValid("()[]{}")) #True
print(test.isValid("(]")) #False