class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while len(str(num))!= 1:
            numList = []
            for num in str(num):
                numList.append(int(num))
            num = sum(numList)

        return num
