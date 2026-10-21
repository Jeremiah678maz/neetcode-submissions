class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        L = 0
        lists = []

        for R in range(len(arr)):
            lists.append(arr[R])
            if R - L >= k:
                lists.pop(0)
                L +=1 
            if len(lists) == k:
                curr = sum(lists) / len(lists)
                if curr >= threshold:
                    res += 1



        return res 

        