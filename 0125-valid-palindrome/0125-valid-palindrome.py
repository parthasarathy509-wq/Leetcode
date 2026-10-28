class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=''
        for m in s :
            if m.isalnum():
                l+=m
        n=l.lower()
        return l.lower()==n[::-1]


        