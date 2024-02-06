class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()

        for a in range(len(nums)-3):
            for b in range(a+1,len(nums)-2):
                res = target - nums[a] - nums[b]
                
                c, d = b+1, len(nums)-1
                while c < d:
                    tmp = nums[c] + nums[d]
                    if tmp == res:
                        ans.add((nums[a], nums[b], nums[c], nums[d]))
                        c += 1
                        while c<d and nums[c] == nums[d]:
                            c += 1
                    elif tmp < res:
                        c += 1
                    elif tmp > res:
                        d -= 1

        return ans