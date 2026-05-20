class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        k = len(nums)
        i=0
        j=0
        result = [1]*k
        for i in range(k):
            p = 1
            for j in range(k):
                if i != j :
                    p = p*nums[j]
            
            result[i] = p        
        return result
