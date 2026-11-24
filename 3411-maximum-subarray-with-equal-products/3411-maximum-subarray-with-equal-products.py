class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            x = y = nums[i]
            prod = 1
            for j in range(i, len(nums)):
                x = gcd(x, nums[j])
                y = lcm(y, nums[j])
                prod *= nums[j]
                if prod == x * y:
                    ans = max(ans, j - i + 1)
        return ans