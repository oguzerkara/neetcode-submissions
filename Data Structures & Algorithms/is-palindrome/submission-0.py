class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = [l for l in list(s.lower()) if l.isalnum()]
        for i in range(len(L)):
            if L[i] != L[-(i+1)]:
                return False
            
        return True
        
            