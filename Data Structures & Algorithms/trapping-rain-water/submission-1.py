class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0 , len(height) -1
        maxL , maxR = 0 , 0
        res = 0

        while l < r:
            maxL = max(maxL , height[l])
            maxR = max(maxR, height[r])

            if height[l] < height[r]:
                cur = min(maxL , maxR) - height[l]
                l += 1

            else:
                cur = min(maxL , maxR) - height[r]
                r -= 1
            
            res += cur

        return res





        