class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sets = set()
        for n in nums:
            if n in sets:
                return True 
            sets.add(n)
        return False
        