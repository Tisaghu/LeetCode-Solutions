class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #Use an array of size 26 to store the count of each letter in the string
        #Use this array as a key in the dictionary
        #The value of the dictionary is a list of strings that have the same count of letters
        ans = {}
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key in ans:
                ans[key].append(s)
            else:
                ans[key] = [s]
        return ans.values()

test = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(test.groupAnagrams(strs)) # [["eat","tea","ate"],["tan","nat"],["bat"]]



        