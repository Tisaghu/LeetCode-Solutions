class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = 0

        for i in range(0,len(s)-1):
            j = i + 1
            replaced = 0
            count = 1
            while j <= len(s)-1:
                if s[j] == s[i]:
                    count += 1
                elif replaced == k:
                    break
                else:
                    replaced += 1
                    count += 1
                j += 1
            res = max(res, count)

        return res

        

test = Solution()
s = "ABBB"
k = 2
print(test.characterReplacement(s,k))