class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        answer=[]
        for i in range(len(prices)):
            discounted=False
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    a=prices[i]-prices[j]
                    answer.append(a)
                    discounted=True
                    break
            if not discounted:
                answer.append(prices[i])
        return answer
        