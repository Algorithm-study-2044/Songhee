class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr2 = [ (a, sum([1 for _ in bin(a) if _ == '1'])) for a in arr ]
        arr3 = sorted(arr2, key=lambda x:(x[1], x[0]))
        return [ a[0] for a in arr3 ]