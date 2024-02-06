class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]
        ans = [0, 1]
        k = 1
        for i in range(2, n+1):
            if i < k*2:
                tmp = 1
                if i-k >= 0:
                    tmp += ans[i-k]
                ans.append(tmp)
            else:
                k *= 2
                ans.append(1)
        return ans

# 다양한 풀이를 함께 보면 좋을듯