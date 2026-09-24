class Solution:
    def hammingWeight(self, n: int) -> int:
        
        n1 = bin(n)

        count = str(n1).count('1')

        return count