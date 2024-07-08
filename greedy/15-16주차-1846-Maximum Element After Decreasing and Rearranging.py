class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr = sorted(arr)[1:]
        n = 1
        for a in arr:
            if abs(n-a) <= 1:
                n = a
            else:
                n += 1
        return n