class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap= {}

        for i , u in enumerate(nums):
            diff = target - u
            if diff in hashmap:
                
                return[hashmap[diff], i] 
        
            hashmap[u] = i