class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # loop and check to see if the number - 1  does not exits
        # if not we use the number and find if number + 1 exist while we increase the length
        # increase the length as we go
         
        #[2,20,4,10,3,4,5]

        res = 0
        newNum = set(nums)
        for n in newNum:
            if n - 1 not in newNum:
                curr = n
                length = 1
                while  curr + length in newNum:
                    length += 1
                res = max(res , length)

        return res
        