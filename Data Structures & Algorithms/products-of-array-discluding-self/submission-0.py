class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(len(nums)):
            j=0
            while j < len(nums):
                if j != i:
                    res[i] = nums[j] * res[i]
                j += 1
            
        return res