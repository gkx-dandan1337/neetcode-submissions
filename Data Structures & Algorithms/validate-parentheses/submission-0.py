class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {
            ")":"(",
            "}":"{",
            "]":"["
        } 

        for char in s:
            if char not in check:
                stack.append(char)
                continue
            else:
                if stack and stack[-1] == check[char]:
                    stack.pop()
                    continue
                else:
                    return False 
        return len(stack) == 0
            