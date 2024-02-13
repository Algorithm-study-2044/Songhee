class Solution:
    def s(self, nums, target, low, high):
        if high < low:
            return -1
        mid = (low+high)//2
        if nums[mid] < target:
            return self.s(nums, target, mid+1, high)
        elif nums[mid] > target:
            return self.s(nums, target, low, mid-1)
        else:
            return mid
        
    def search(self, nums: List[int], target: int) -> int:
        return self.s(nums, target, 0, len(nums)-1)


    # 재귀 말고 반복문으로 구현
    def search_while(self, arr: List[int], target: int) -> int:

        l, h = 0, len(arr)-1

        while l <= h:
            m = l + (h-l)//2

            if arr[m] == target:
                return m
            elif arr[m] < target:
                low = m + 1
            else:
                high = m - 1

        return -1