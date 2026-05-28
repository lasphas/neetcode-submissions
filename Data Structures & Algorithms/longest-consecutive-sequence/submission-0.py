class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums : 
            return 0
        unique = sorted(list(set(nums)))
        c = 1
        i = 0
        s = []
        for i in range(len(unique) - 1) :
            if unique[i+1] - unique[i] == 1 :
                c += 1
            else :
                s.append(c)
                c = 1
        s.append(c)
        return max(s)
        