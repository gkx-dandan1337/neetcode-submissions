class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for char in tokens:
            if char not in ("+" , "-", "*", "/"):
                stack.append(char)
            else:
                if char == "+":
                    first, second = int(stack.pop()), int(stack.pop())
                    stack.append(first+second)
                elif char == "*":
                    first, second = int(stack.pop()), int(stack.pop())
                    stack.append(first*second)
                elif char == "/":
                    first, second = int(stack.pop()), int(stack.pop())
                    stack.append(int(second/first))
                else:
                    first, second = int(stack.pop()), int(stack.pop())
                    stack.append(int(second-first))
        return int(stack[0])
                