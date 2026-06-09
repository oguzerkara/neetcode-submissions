class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count, max_count, i = 1, 1, 1
        arr = sorted(set(nums))
        while i < len(arr):
            if arr[i] - arr[i-1] != 1:
                count = 1
            else: 
                count +=1
            if count > max_count:
                max_count = count
            i += 1
        return max_count
            
