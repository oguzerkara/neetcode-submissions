class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tmp = prices[0]
        res, max_res = 0, 0
        for p in prices:
            tmp = min(p,tmp)
            if p > tmp:
                res = p - tmp
                max_res = max(res, max_res)

        return max_res