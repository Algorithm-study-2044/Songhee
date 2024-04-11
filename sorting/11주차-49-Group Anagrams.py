# Amazon Interview Question

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs = sorted(strs)
        word = defaultdict(list)
        for st in strs:
            w = ''.join(sorted(list(st)))
            word[w].append(st)
        ans = []
        for k, v in word.items():
            ans.append(v)
        return ans