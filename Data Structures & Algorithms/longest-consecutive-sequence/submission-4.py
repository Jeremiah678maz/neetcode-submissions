class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort = set(nums)
        longest = 0

        for n in sort:
            if n - 1 not in sort:
                length = 1
                while n + length in sort:
                    length += 1
                longest = max(length, longest)
        return longest


        