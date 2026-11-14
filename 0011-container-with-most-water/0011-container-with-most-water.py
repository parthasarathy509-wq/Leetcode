class Solution:
    def maxArea(self, height: list[int]) -> int:
        best=0
        l=0
        r=len(height)-1
        while l<r:
            wid=(r-l) * min(height[l],height[r])
            if wid>best:
                best=wid
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return best