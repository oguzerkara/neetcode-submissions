class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s_nums = sorted(set(nums))
        i = 1
        res_tm = [s_nums[0]]
        res = []

        while i < len(s_nums):
            if s_nums[i]  == s_nums[i-1] +1:
                res_tm.append(s_nums[i])
            else: 
                if len(res_tm) > len(res):
                    res = res_tm
                res_tm = [s_nums[i]]
            i += 1
        if len(res_tm) > len(res):
            res = res_tm 
        return len(res)
