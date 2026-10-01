class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {"{": "}", "[": "]", "(": ")"}

        stack = []

        for char in s:
            if char in openToClose:
                stack.append(char)

            else:
                if stack == [] or openToClose[stack.pop()] != char:
                    return False

        return True if stack == [] else False
                



            



        
