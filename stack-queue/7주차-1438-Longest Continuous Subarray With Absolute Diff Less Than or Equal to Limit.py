# 풀이 참고, 구글 기출 문제

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # use i, j as the start and the end of the sliding window
        maxLen, i = 0, 0
        
        # minQ keeps track of the min values in the sliding window
        # maxQ keeps track of the max values in the sliding window
        minQueue, maxQueue = collections.deque(), collections.deque()
        
        for j in range(len(nums)):
            # remove from minQ if the last value in the queue is larger
            while minQueue and minQueue[-1] > nums[j]:
                minQueue.pop()
            minQueue.append(nums[j])
            
            # remove from maxQ if the last value in the queue is smaller
            while maxQueue and maxQueue[-1] < nums[j]:
                maxQueue.pop()
            maxQueue.append(nums[j])
            
            # if the diff is within the limit, we can move the right point of the sliding window
            if maxQueue[0] - minQueue[0] <= limit:
                maxLen = max(maxLen, j-i+1)
            # if the diff is beyond the limit, we need to move the left point of the sliding window
            # and also update the queues accordingly 
            else:
                if maxQueue[0] == nums[i]:
                    maxQueue.popleft()
                if minQueue[0] == nums[i]:
                    minQueue.popleft()
                i += 1
        return maxLen