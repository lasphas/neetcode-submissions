class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        def count1(n1):
            n2 = bin(n1)

            count = str(n2).count('1')

            return count
        
        for i in range(0,n+1):
            res.append(count1(i))
            
        return res