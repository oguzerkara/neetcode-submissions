class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ch = {}
        for i in strs:
            key = tuple(sorted(list(i)))
            if key not in ch:
                ch[key]=[]
            ch[key].append(i)
        return list(ch.values())