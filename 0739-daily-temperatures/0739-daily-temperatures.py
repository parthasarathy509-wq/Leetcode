class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res=[0]*len(temperatures)
        s=[]
        t=temperatures
        for i in range(len(t)):
            while s and t[i]>t[s[-1]]:
                pope=s.pop()
                res[pope]=i-pope
            s.append(i)
        return res    