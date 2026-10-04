class Solution:
    def checkValidString(self, s: str) -> bool:
        
        minopen = 0
        maxopen = 0

        for char in s:
            if char == "(":
                minopen += 1
                maxopen += 1
            elif char == ")":
                minopen -= 1
                maxopen -= 1
            
            else :
                minopen -= 1
                maxopen += 1
            
            if maxopen < 0:
                return False
            if minopen < 0:
                minopen = 0
        return minopen == 0