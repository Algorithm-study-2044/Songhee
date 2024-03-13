# heapq.nsmallest(n, data):  k번째까지 빼주세요를 간단하게 줄인 함수 (유용하다)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        tmp = [(point[0]*point[0]+point[1]*point[1], point) for point in points]
        arr = heapq.nsmallest(k, tmp)
        return [a[1] for a in arr]