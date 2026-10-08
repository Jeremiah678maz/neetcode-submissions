class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        temps = temperatures
    
        stack = []
        res = [0] * len(temps)

        for i in range(len(temps)):
            while stack and temps[stack[-1]] < temps[i]:
                ind = stack.pop()
                res[ind] = i - ind
            stack.append(i)

        return res

        