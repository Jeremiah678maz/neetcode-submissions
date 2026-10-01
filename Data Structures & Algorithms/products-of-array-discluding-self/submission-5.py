class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lmult = 1
        rmult = 1
        n = len(nums)
        larr = [0] * n
        rarr = [0] * n
        
        for i in range(n):
            j= -i -1
            larr[i] = lmult
            rarr[j] = rmult
            lmult *= nums[i]
            rmult *= nums[j]

        return [l*r for l, r in zip(larr, rarr)]
