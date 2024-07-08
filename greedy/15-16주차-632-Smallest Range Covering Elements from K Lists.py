# 어려움

N = 5
ptr = [0 for i in range(501)]

class Solution:
    def smallestRange(self, nums):
        if not nums:
            return []

        # Initialize the min heap
        min_heap = []
        current_max = float('-inf')

        # Add the first element of each list to the heap
        for i in range(len(nums)):
            heappush(min_heap, (nums[i][0], i, 0))
            current_max = max(current_max, nums[i][0])

        # Initialize the smallest range as very large
        smallest_range = [float('-inf'), float('inf')]

        while min_heap:
            min_val, list_idx, ele_idx = heappop(min_heap)
            
            # Update the smallest range if the current range is smaller
            if current_max - min_val < smallest_range[1] - smallest_range[0]:
                smallest_range = [min_val, current_max]
            
            # If we have exhausted any list, we break out of the loop
            if ele_idx + 1 == len(nums[list_idx]):
                break
            
            # Add the next element of the list to the heap
            next_val = nums[list_idx][ele_idx + 1]
            heappush(min_heap, (next_val, list_idx, ele_idx + 1))
            current_max = max(current_max, next_val)
        
        return smallest_range

    