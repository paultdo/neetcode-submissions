class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                num = int(stack[-2]) + int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(num)
            elif t == "-":
                num = int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(num)
            elif t == "*":
                num = int(stack[-2]) * int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(num)
            elif t == "/":
                num = int(stack[-2]) / int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(int(num))
            else:
                stack.append(t)
        return int(stack[-1])
