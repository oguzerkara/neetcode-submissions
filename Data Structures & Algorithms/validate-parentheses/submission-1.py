class Solution:
    def isValid(self, s: str) -> bool:
        k = {'{':'}', '[':']', '(':')'}
        stack = []

        for key in list(s):
            if key in k:
                stack.append(k[key])
            else:
                if not stack or key != stack.pop():
                    return False
        return not stack