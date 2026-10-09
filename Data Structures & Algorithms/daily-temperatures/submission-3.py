class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        res = [0] * len(temp)

        stack  = []

        for i in range(len(temp)):
            while stack and temp[stack[-1]] < temp[i]:
                ind = stack.pop()
                res[ind] = i - ind
            stack.append(i)
        return res
    

        