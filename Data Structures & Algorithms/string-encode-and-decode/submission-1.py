class Solution:

    def encode(self, strs: List[str]) -> str:
        res = str()
        for s in strs:
            res += str(len(s))+"#"+s
        return res
    def decode(self, s: str) -> List[str]:
        i=0
        res = []
        while i < len(s):
            j=i
            while s[j] != "#":
                j += 1
            num = int(s[i:j])
            i = j +1
            res.append(s[i: i+num])
            i += num
        return res