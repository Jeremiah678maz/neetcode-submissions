class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        sort = set(nums)

        for n in sort:
            if n - 1 not in sort:
                length = 1
                while (n + length) in sort:
                    length += 1
                res = max(res,length)
        return res
        