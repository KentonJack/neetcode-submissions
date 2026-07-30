class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                prof = prices[r] - prices[l]
                res = max(res, prof)
        return res