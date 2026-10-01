import operator 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': lambda a, b: int(a / b),
}

        
        stack = []
    
        for char in tokens:
            if char in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[char](a, b))
            else:
                stack.append(int(char))

        return stack[0]
