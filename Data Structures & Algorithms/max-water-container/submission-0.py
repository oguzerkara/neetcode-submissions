class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        water =0 
        tmp = 0
        while i < len(heights)-1:
            j = i+1
            while j < len(heights):
                tmp = min(heights[i], heights[j])*(j-i)
                if tmp > water:
                    water = tmp
                j += 1
            i += 1
        return water