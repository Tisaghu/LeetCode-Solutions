class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        #initiate two pointers
        l = 0
        hash = []
        count = 1
        longest = 1

        while l in range(0,len(s)):
            hash.append(s[l])
            r = l+1
            while r in range(0,len(s)):
                if s[r] in hash:
                    l = r-1
                    count = 1
                    hash = []
                    break
                else:
                    hash.append(s[r])
                    count +=1
                    longest = max(longest,count)
                    r+=1
            l += 1
        
        return longest

            

        


test = Solution()
print(test.lengthOfLongestSubstring("aab"))
print(test.lengthOfLongestSubstring(""))
print(test.lengthOfLongestSubstring("abcabcbb")) #3 "abc"