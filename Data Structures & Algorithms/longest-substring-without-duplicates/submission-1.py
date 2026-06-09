class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = []
        max_c = 0
        L = list(s)
        for i in L:
            if i not in cache:
                cache.append(i)
            else:
                 max_c = max(len(cache), max_c)
                 index = cache.index(i)
                 cache = cache[index + 1:]
                 cache.append(i)
        return max(len(cache), max_c)