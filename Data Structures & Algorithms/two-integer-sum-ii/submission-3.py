class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l , r = 0 , len(numbers) - 1
        n = numbers

        res = []

        while l < r:
            if n[l] + n[r] > target:
                r -= 1

            elif n[l] + n[r] < target:
                l += 1

            elif n[l] + n[r] == target:
                return [l + 1 , r + 1]

