class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        count = Counter(nums)
        
        def counter(n):
            return (count[n],-n)
        nums.sort(key=counter)

        return nums