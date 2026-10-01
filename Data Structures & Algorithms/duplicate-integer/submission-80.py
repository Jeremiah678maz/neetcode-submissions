class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 1 build hashset to store duplicate, 2 we iterate thru the arr and add all the number into the hashset , 3 if we see that nums already exixted then we return true

        seen = set()
        for s in nums:
            if s in seen:
                return True
            seen.add(s)

        return False