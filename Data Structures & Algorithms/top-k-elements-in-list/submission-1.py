class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        numcount = {}
        result = []

        for num in nums :
            numcount[num] = numcount.get(num,0) + 1
        
        sorted_num = dict(sorted(numcount.items(), key = lambda item: item[1] , reverse = True))
        key_list = list(sorted_num.keys())

        for i in range(k):
            result.append(key_list[i])
        
        return result

