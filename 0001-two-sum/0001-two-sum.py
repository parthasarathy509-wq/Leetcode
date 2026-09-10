class Solution :
    def twoSum(self,nums,target):
        mem={}
        for i,num in enumerate(nums):
            ma=target-num
        
            if ma in mem:
                return [mem[ma],i]
            
            mem[num]=i

                