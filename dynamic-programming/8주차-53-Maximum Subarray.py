class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        dp_array = [0] * len(nums)
        dp_array[0] = nums[0]
        
        for idx in range(1,len(nums)):
            prev_max = dp_array[idx-1]
            crnt_val = nums[idx]
            
            connected_sum = prev_max + crnt_val
            max_sub = max(connected_sum , crnt_val)
            dp_array[idx] = max_sub
            
        max_sum = max(dp_array)
        return max_sum