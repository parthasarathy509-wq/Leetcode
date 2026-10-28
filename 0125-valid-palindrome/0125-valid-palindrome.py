class Solution:
    def isPalindrome(self, s: str) -> bool:
        char=[]
        for m in s :
            if m.isalnum():
                char.append(m.lower())
        l="".join(char)
        return l==l[::-1]


        