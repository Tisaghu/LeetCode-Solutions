class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
            
test = Solution()
print(test.lengthOfLongestSubstring("aab"))
print(test.lengthOfLongestSubstring(""))
print(test.lengthOfLongestSubstring("abcabcbb")) #3 "abc"