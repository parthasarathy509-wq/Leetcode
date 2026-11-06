class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l=0
        r=len(numbers)-1
        while l<r:
            current=numbers[l]+numbers[r]
            if current == target:
                return [l+1,r+1]
            if current>target:
                r-=1
            else:
                l+=1