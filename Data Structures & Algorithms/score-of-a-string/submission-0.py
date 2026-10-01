class Solution:
    def scoreOfString(self, s: str) -> int:
        count = 0
        for i in range(len(s)-1):
            math = abs(ord(s[i + 1]) - ord(s[i]))
            count += math
        return count

        