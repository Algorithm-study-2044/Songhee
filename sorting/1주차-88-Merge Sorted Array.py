# 다시 풀어보기

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[n:] = nums1[:m]
        n1 = n
        n2 = 0
        i = 0
        while n1 < m+n and n2 < n:
            if nums1[n1] < nums2[n2]:
                nums1[i] = nums1[n1]
                n1 += 1
            else:
                nums1[i] = nums2[n2]
                n2 += 1
            i += 1
        if n2 < n:
            nums1[i:] = nums2[n2:]