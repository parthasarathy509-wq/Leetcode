class Solution:
    def twoSum(self,l, t):
        for i in range(len(l)):
            f = l[i]
            for j in range(i + 1, len(l)):
                g = l[j]
                if f + g == t:
                    return [i, j]
                else:
                    continue