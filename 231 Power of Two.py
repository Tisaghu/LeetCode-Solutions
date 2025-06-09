class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        else:
            n_bin = bin(n)[2:] #remove the '0b' prefix
            prev_bin = bin(n-1)[2:]
            return (n & (n - 1)) == 0
            