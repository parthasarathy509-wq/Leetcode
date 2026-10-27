class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [1] * n
        
        # Pass 1: Calculate Prefix Products
        # ans[i] will store the product of all elements to the left of i
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]
            
        # Pass 2: Calculate Suffix Products & Multiply
        # Multiply ans[i] by the running product of all elements to the right of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
            
        return ans

        