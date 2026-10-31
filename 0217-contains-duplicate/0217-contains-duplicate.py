class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        a={}
        for i in nums:
            count=1
            if i in a:
                count+=1
                a[i]=count
            a[i]=count
        true=False
        for j,k in a.items():
            if k>1:
                true=True
        return true
        

        
