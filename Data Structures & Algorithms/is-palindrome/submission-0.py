class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if not s :
            return True

        s_new = ""
        for char in s :
            if char.isalnum():
                s_new += char.lower()
        

        reversed_str = s_new[::-1]

        if s_new == reversed_str:
            return True
        else :
            return False

