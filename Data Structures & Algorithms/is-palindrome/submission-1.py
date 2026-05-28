class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if not s :
            return True

        s = "".join(char.lower() for char in s if char.isalnum())
        

        reversed_str = s[::-1]

        if s == reversed_str:
            return True
        else :
            return False

