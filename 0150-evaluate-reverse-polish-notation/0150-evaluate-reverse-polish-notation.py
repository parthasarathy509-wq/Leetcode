import math
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        s=[]
        op=['+','-','*','/']
        for i in tokens:
            if i in op:
                right=s.pop()
                left=s.pop()
                if i=='+':
                    right+=left
                    s.append(right)
                elif i=='-':
                    left-=right
                    s.append(left)
                elif i=='*':
                    left*=right
                    s.append(left)
                elif i =='/':
                    left/=right
                    s.append(math.trunc(left))
            else:
                s.append(int(i))
        return s[-1]