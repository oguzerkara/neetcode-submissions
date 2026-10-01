class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = dict()
        fun = lambda x: tuple(sorted(list(x)))
        for st in strs:
            if fun(st) not in seen:
                seen[fun(st)] = []
            seen[fun(st)].append(st)
        return list(seen.values())

