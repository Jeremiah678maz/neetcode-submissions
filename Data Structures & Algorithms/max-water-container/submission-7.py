class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res = 0
        l = 0
        r = len(heights) -1

        while l < r:
            minRL = min(heights[l] , heights[r])
            area =  ( r - l) * minRL

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            res = max(res , area)

        return res
        