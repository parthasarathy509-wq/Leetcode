class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        k=sorted(set(nums))
        l=0
        r=1
        count=1
        max_count=1
        while r<len(k):
            if k[l]==(k[r]-1):
                count+=1
                max_count=max(count,max_count)
            else:
                count=1
            l+=1
            r+=1
        return max_count
        