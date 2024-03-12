class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = Counter(arr)
        for (key, value) in sorted(cnt.items(), key=lambda x: x[1]):
            cnt[key] = 0 if k>value else value-k
            k = k-value if k>value else 0
            if not k:
                print(cnt)
                print(set(cnt.elements()))
                return len(set(cnt.elements()))
        return 0
