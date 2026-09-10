class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a={}
        for i,n in enumerate(nums):
            if n in a :
                return True
            else :
                a[n]=i
                continue
        return False 
