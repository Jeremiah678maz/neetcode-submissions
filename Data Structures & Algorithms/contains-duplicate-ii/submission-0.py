class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        [ 1, 2, 3 , 4 ,1]  k = 3
          0  1  2   3
          L
          R

          window = {2, 3 ,4}

       # check for window size
       # check if num in set if not we add 
        """
        window = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False
