class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        
        cur = 1
        for n in range(len(s)-1):
            if s[n] == '(':
                if s[n+1] == ')':
                    score += cur
                cur *= 2
            else:
                cur /= 2
        
        return int(score)