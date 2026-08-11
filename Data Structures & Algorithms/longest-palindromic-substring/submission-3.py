class Solution:
    def longestPalindrome(self, s: str) -> str:

        n=len(s)
        a=""
        for i in range(n):
            p=i-1
            q=i+1
            while (p>=0 and q<n and s[p]==s[q]):
                p-=1
                q+=1
            if len(s[p+1:q])>len(a):
                a=s[p+1:q]
            p=i-1
            q=i
            while(p>=0 and q<n and s[p]==s[q]):
                p-=1
                q+=1
            if len(s[p+1:q])>len(a):
                a=s[p+1:q]
        return a
                