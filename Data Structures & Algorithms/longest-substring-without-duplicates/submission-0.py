class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        newVar = set()

        res = 0
        L = 0

        for R in range(len(s)):
            while s[R] in newVar:
                newVar.remove(s[L])
                L += 1
            newVar.add(s[R])

            res = max(res , R - L + 1)
        

        return res



