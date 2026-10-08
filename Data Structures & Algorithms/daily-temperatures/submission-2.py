class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tem = temperatures
        res = [0] * len(tem)
        stack= []

        for i in range(len(tem)):
            while stack and tem[stack[-1]] < tem[i]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res

        