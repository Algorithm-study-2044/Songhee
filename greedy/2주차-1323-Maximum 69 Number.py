class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = [int(n) for n in str(num)]
        ans = 0
        first6 = True
        for n in nums:
            if n == 6 and first6:
                ans = ans*10 + 9
                first6 = False
            else:
                ans = ans*10 + n
        return ans