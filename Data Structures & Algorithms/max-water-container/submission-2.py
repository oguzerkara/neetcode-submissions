class Solution:
    def maxArea(self, heights: List[int]) -> int:


        mul = 0

        for l in range(len(heights)-1):
            r = len(heights)-1
            while l<r:
                
                mul = max(min(heights[l], heights[r]) * (r-l), mul)
                r -= 1
        return mul
            