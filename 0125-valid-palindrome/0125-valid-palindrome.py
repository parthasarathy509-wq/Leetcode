class Solution:
    def isPalindrome(self, s: str) -> bool:
        c=[]
        for i in s:
            if i.isalnum():
                c.append(i.lower())
        l="".join(c)
        return l==l[::-1]



        