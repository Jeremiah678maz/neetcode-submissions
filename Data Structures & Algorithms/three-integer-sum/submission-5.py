class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        num = sorted(nums)
        # [-4, -1, -1 ,0,1, 2 ]
        res = []

        for i , a in enumerate(num):

            if a > 0:
                break 
            if i > 0  and a == num[i - 1]:
                continue 

            l = i + 1
            r = len(num) -1

            while l < r:
                threeSum = a + num[r] + num[l]
                if threeSum > 0:
                    r -= 1

                elif threeSum < 0:
                    l +=1

                else:
                    res.append([a , num[l], num[r]])
                    l += 1
                    r -= 1
                    while num[l] == num[l - 1] and l < r:
                        l += 1

        return res