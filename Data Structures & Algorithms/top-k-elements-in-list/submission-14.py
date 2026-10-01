class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        freq = {}

        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)

        sort = sorted(freq.items(), key = lambda pair: pair[1], reverse = True)


        for j in range(k):
            res.append(sort[j][0])
        return res
            