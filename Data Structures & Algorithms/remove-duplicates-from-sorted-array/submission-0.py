class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num = sorted(set(nums))
        for i in range(len(num)):
            nums[i] = num[i]
        

        return len(num)
  