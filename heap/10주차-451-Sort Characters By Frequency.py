class Solution:
    def frequencySort(self, s: str) -> str:
        heap = []
        for v, c in collections.Counter(s).items():
            heapq.heappush(heap,[-c,v])
        res = ""
        while heap:
            c, v = heapq.heappop(heap)
            res += v*-c
        return res