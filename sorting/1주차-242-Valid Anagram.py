from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return not (set(s)-set(t)) and not (set(t)-set(s)) and len(s) == len(t) # 43/48 pass
        if len(s) != len(t) or set(s)-set(t) or set(t)-set(s):
            return False
        ref = list(set(s))
        ss = Counter(s)
        tt = Counter(t)
        for r in ref:
            if ss[r] != tt[r]:
                return False
        return True

    # 더 쉬운 풀이...
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t
        