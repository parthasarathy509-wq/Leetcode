class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        a={}
        for i,l in enumerate(nums):
            m=target-l
            if m in a:
                return a[m],i
            a[l]=i

        