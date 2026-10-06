class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort = set(nums)

        longest = 0 

        for n in sort:
            if (n - 1 ) not in sort:
                count = 1
                while n + count in sort:
                    count += 1
                longest = max(count , longest)

        return longest

            


        