class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc += str(len(s))+"#"+s
        return enc

    def decode(self, s: str) -> List[str]:
        dec =[]
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            num = int(s[i:j])
            i = j+1
            dec.append(str(s[i:i+num]))
            i+= num
        return dec
                


