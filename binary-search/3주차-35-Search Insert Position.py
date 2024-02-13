class Solution:
    def search(self, nums, target, low, high):
        if high < low:
            return low
        mid = (low+high)//2
        # print(f'low: {low}, mid: {mid}, high: {high}, nums[mid]: {nums[mid]}')
        
        if nums[mid] > target:
            return self.search(nums, target, low, mid-1)
        elif nums[mid] < target:
            return self.search(nums, target, mid+1, high)
        else:
            return mid

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.search(nums, target, 0, len(nums)-1)
        
