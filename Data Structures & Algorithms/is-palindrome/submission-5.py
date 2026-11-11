class Solution:
    def isPalindrome(self, s: str) -> bool:
        sn = "".join(char.lower() for char in s if char.isalnum())
        l = 0
        r = len(sn) - 1

        while l < r:

            if sn[l] != sn[r]:
                return False
            l += 1
            r -= 1
        return True

        