from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        q = deque()
        for i in s:
            if i not in q:
                q.append(i)
            else:
                index = q.index(i)
                for j in range(index + 1):
                    q.popleft()
                q.append(i)
            max_len = max(max_len, len(q))
        return max_len