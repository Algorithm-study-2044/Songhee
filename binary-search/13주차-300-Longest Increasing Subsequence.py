from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]

        for num in nums[1:]:
            if sub[-1] < num:
                sub.append(num)
            else:
                i = bisect_left(sub, num)
                sub[i] = num
            print(sub)

        return len(sub)