class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        freq = {}

        L = 0

        for R in range(len(s)):
            freq[s[R]] = 1 + freq.get(s[R], 0)

            while (R - L + 1) - max(freq.values()) > k:
                freq[s[L]] -= 1
                L += 1
            res = max (res ,R - L + 1)

        return res



