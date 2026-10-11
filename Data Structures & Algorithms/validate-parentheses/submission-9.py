class Solution:
    def isValid(self, s: str) -> bool:
        
        openToClose = {"{":"}" , "(":")", "[":"]" }

        stack = []

        for c in s:
            if c in openToClose:
                stack.append(c)
            elif not stack or openToClose[stack.pop()] != c:
                return False
        return True if not stack else False
