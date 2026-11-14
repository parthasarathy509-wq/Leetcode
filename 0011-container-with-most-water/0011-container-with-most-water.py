class Solution:
    def maxArea(self, height: list[int]) -> int:
        cur=[]
        l=0
        r=len(height)-1
        while l<r:
            le=r-l
            wid=min(height[l],height[r])
            max_cur=le*wid
            cur.append(max_cur)
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return max(cur)