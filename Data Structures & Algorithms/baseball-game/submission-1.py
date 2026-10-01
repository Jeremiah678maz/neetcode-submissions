class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # make new array
        # loop thru op 
        # if else statement  using push pop and also peek
        # interate thru and all all 
        stack = []

        for i in range(len(operations)):
            if operations[i].lstrip("-").isdigit():
                stack.append(int(operations[i]))
            elif operations[i] == "D":
                stack.append(stack[-1] * 2)
            elif operations[i] == "+":
                stack.append(stack[-1] + stack[-2])
            elif operations[i] == "C":
                stack.pop()

        return sum(stack)





        