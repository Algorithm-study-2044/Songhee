class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        ans = 0
        while j-i > 0:
            ans = max(ans, (j-i)*min(height[i], height[j]))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return ans

    # time limit exceeded 51/62 testcases passed
    def maxArea1(self, height: List[int]) -> int:
        ans = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                ans = max(ans, (j-i)*min(height[i], height[j]))
        return ans