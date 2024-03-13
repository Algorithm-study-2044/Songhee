# heap2 = [4, 1, 7, 3, 8, 5]
# heapq.heapify(heap2)
# print(heap2)
# [1, 3, 5, 4, 8, 7]

# heapq.nsmallest(n, data):  k번째까지 빼주세요를 간단하게 줄인 함수 (유용하다)

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        tmp = [(abs(a-x), a) for a in arr]
        arr = heapq.nsmallest(k, tmp)
        return sorted([a[1] for a in arr])