class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            elif arr[mid] > arr[mid + 1]:
                r = mid - 1
        return l
    
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        s = sorted(set(A), reverse=True)
        for n in s:
            i = A.index(n)
            if A[i-1] < n > A[i+1]:
                return i