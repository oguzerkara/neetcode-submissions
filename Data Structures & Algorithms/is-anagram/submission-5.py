class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds, dt = {}, {}
        if len(s) != len(t): return False

        for i in range(len(s)):
            ds[s[i]] = ds.get(s[i],0)+1
            dt[t[i]] = dt.get(t[i],0)+1
        
        return ds == dt