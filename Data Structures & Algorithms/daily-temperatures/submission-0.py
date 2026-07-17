class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]* len(temperatures)

        #loop from the back 
        stack = [] #stores (temp, index)

        for i in range(len(temperatures)-1,-1,-1):
            temp = temperatures[i]

            while stack and stack[-1][0] <= temp:
                stack.pop()
            
            if stack:
                days = stack[-1][1] - i 
                res[i] = days
            stack.append((temp, i))
        return res

            