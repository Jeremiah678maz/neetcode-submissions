class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) -1 
        res = 0
        while l < r:
            wL,wR = heights[l], heights[r]
            length = r - l
            area = (min(wL, wR))  * length
            res = max(area, res)
            
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return res
        