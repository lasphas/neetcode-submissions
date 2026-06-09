class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        stack = []
        hsmap = {")" : "(", "}" : "{" , "]" : "["}

        for c in s:
            if c in hsmap :
                if stack and stack[-1] == hsmap[c] :
                    stack.pop()
                else :
                    return False
            else :
                stack.append(c)
        return True if not stack else False        
        