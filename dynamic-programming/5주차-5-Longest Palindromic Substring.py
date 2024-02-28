# 풀이 참고,

# 팰린드롬 확인 코드
# if s[::-1] == s:
#     return s

# 팰린드롬 찾기 코드
# def spread(i,j):
#     while i>=0 and j<n and s[i]==s[j]:
#         i-=1
#         j+=1
#     return s[i+1:j]

class Solution:
    def longestPalindrome(self, s: str) -> str:
    
        n=len(s)
        res=0
        
        def spread(i,j):
            while i>=0 and j<n and s[i]==s[j]:
                i-=1
                j+=1
            return s[i+1:j]
        
        res=""
        for i in range(n):
            res=max(spread(i,i), spread(i,i+1),res, key=len)
        
        return res