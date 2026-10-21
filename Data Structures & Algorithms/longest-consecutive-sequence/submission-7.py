class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = 0 
        numSort = set(nums)

        for n in nums:
            if n - 1 not in numSort:
                length  = 1
                while n + length in numSort:
                    length += 1
                res = max(res , length)
        return res 

        