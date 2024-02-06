class Solution:
    def minimumSum(self, num: int) -> int:
        d1, d2, n1, n2 = sorted([int(n) for n in str(num)])
        return d1*10+d2*10+n1+n2