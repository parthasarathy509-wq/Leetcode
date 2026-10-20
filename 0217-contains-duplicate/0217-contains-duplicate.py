class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        a={}
        for i,n in enumerate(nums):
            if n in a:
                return True 
            a[n]=i
        return False 
        