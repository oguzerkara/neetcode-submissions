class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = dict()
        bucket = [[] for _ in range(len(nums)+1)]
        res = []
        for n in nums:
            seen[n] = seen.get(n, 0) + 1
        for key, value in seen.items():
            bucket[value].append(key)
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res
        
        
        