class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        a={}
        for i ,n in enumerate(numbers):
            miss=target-n
            if miss in a:
                return [a[miss]+1,i+1]
            a[n]=i