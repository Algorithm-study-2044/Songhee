class Solution:
    def romanToInt(self, s: str) -> int:
        ans, i = 0, 0
        d = {'I':1, 'V':5, 'IV':4, 'IX':9, 
            'X':10, 'L':50, 'XL':40, 'XC':90, 
            'C':100, 'CD':400, 'CM':900, 'D':500, 'M':1000}
        while True:
            if i == len(s)-1:
                ans += d[s[i]]
                break
            elif i > len(s)-1:
                break
            x, y = s[i], s[i+1]
            if f'{x}{y}' in d:
                ans += d[f'{x}{y}']
                i += 2
            else:
                ans += d[x]
                i += 1
        return ans