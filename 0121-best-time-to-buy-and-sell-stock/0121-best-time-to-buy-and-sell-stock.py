class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini=prices[0]
        maxi=0
        for i in range(len(prices)):
            if mini>prices[i]:
                mini=min(mini,prices[i])
            elif prices[i]-mini>maxi:
                maxi=max(maxi,(prices[i]-mini))
        return maxi