class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charlist = list()
        l = 0
        res = 0
        for r in range(len(s)) :
            while s[r] in charlist :
                charlist.remove(s[l])
                l += 1
            charlist.append(s[r])
            res = max(res , r-l +1)
        return res


        