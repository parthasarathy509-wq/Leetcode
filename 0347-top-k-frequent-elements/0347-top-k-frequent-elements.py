class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        a={}
        l=[]
        for i in range(len(nums)):
            count=1
            if nums[i] in a:
                count+=a[nums[i]]
                a[nums[i]]=count
            a[nums[i]]=count
        for i in range(k):
            top =max(a.values())
            k=next((k for k ,v in a.items() if v==top),None)
            l.append(k)
            a.pop(k)
        return l
        