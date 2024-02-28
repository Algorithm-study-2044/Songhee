from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)

        n = []
        for c in cnt:
            n.append(cnt[c])
        n = sorted(n, reverse=True)

        ans = 0
        for i in range(1, len(n)):
            if n[i] == 0:
                break
            if n[i-1] <= n[i]:
                ans += n[i]-n[i-1]
                n[i] = max(n[i-1]-1, 0)
                ans += n[i-1]-n[i]
        return ans