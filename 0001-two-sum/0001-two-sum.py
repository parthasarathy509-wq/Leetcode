class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        a={}
        for i,n in enumerate(nums):
            miss=target-n
            if miss in a :
                return (a[miss],i)
            a[n]=i
        