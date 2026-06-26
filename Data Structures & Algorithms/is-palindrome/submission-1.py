class Solution:
    def isPalindrome(self, s: str) -> bool:
        wrd = [l for l in list(s.lower()) if l.isalnum()]
        return wrd == wrd[::-1]