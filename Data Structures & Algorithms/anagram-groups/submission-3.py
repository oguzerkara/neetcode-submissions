class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = dict()
        seen = dict()
        for st in strs:
            if tuple(sorted(list(st))) in seen:
                seen[tuple(sorted(st))].append(st)
            else: seen[tuple(sorted(st))] = [st]
        return list(seen.values())
