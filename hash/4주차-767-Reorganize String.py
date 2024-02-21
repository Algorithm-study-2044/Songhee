from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        res = ""
        while len(c.keys()) > 1:
            f, s = c.most_common(2)
            if s[1] > 0:
                c[f[0]] -= 1
                c[s[0]] -= 1
                res += (f[0] + s[0])
            else:
                del c[s[0]]
                if f[1] == 0:
                    del c[f[0]]
        if c.total() > 1:
            return ""
        if c.total() == 1:
            res += c.most_common(1)[0][0]
        return res
        