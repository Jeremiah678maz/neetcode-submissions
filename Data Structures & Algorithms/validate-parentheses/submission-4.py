class Solution:
    def isValid(self, s: str) -> bool:
        opentoClose = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        stack = []
        
        for char in s:
            if char in opentoClose:
                stack.append(char)
            else:
                if stack == [] or opentoClose[stack.pop()] != char:
                    return False

        return True if stack == [] else False