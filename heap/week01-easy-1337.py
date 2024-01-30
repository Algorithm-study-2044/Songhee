class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strn = [(i, sum(mat[i])) for i in range(len(mat))]
        strn = sorted(strn, key=lambda x: (x[1], x[0]))
        # print(strn)
        return [s[0] for s in strn][:k]