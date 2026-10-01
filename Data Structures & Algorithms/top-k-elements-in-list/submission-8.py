class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hashmap = {}
        
        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i],0)

        sort = sorted(hashmap.items(), key = lambda pair: pair[1], reverse = True)

        for j in range(k):
            res.append(sort[j][0])

        return res 

    