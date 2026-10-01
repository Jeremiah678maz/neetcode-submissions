class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        seen = {}

        for i in range(len(nums)):
            seen[nums[i]] = 1 + seen.get(nums[i], 0)

        sort = sorted(seen.items(), key = lambda pair : pair[1], reverse = True)

        for j in range((k)):
            res.append(sort[j][0])
        
        return res
