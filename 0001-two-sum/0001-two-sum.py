class Solution :
    def twoSum(self,nums,target):
        dictt ={}
        for i,n in enumerate(nums):
            miss=target-n
            if miss in dictt:
                return [dictt[miss],i]
            dictt[n]=i
