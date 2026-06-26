class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in range(len(nums))]
        bucket = []

        for n in range(len(nums)):
            for i in range(len(nums)):
                if n != i:
                    res[n] = res[n] * nums[i]
        return res

