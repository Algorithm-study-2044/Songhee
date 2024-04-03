class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        counter = [0 for i in range(len(T))]
        stack = [0]
        
        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]: 
                top = stack.pop()
                counter[top] = i - top
            stack.append(i)
        
        return counter
