class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # 1. Calculate area using your logic
            current_area = min(height[left], height[right]) * (right - left)
            
            # 2. Keep track of the max
            max_water = max(max_water, current_area)
            
            # 3. Greedily move the pointer of the shorter wall inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water