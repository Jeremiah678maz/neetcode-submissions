class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort  = set(nums)
        longest = 0

        for n in sort:
            if n - 1 not in sort:
                lenght = 1
                while n + lenght in sort:
                    lenght += 1 
                longest = max(lenght , longest)
        return longest

        