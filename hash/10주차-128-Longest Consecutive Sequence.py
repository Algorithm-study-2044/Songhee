class Solution:
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     # 69 / 75 testcases passed
    #     d = dict()
    #     for num in nums:
    #         if num in d:
    #             continue
    #         d[num] = 1
    #     max_cnt = 0
    #     for num in nums:
    #         cnt = 0
    #         while num in d:
    #             cnt += 1
    #             num += 1
    #             if d[num]
    #         max_cnt = max(max_cnt, cnt)
    #     return max_cnt

    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        if len(set(nums)) == 1:
            return 1 
    
        s = set()
        ans = 0
    
        # Hash all the array elements
        for num in nums:
            s.add(num)
    
        # check each possible sequence from the start
        # then update optimal length
        for i in nums:
    
            # if current element is the starting
            # element of a sequence
            if (i-1) not in s:
    
                # Then check for next elements in the
                # sequence
                j = i
                while(j in s):
                    j += 1
    
                # update  optimal length if this length
                # is more
                ans = max(ans, j-i)
        return ans

# leetcode solution: n-1이 없는 경우(=시작점일 때)만 찾기 시작하면 count 횟수를 획기적으로 줄일 수 있다.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        for n in nums:
            if n - 1 not in nums:
                m = n + 1
                while m in nums:
                    m += 1
                best = max(best, m - n)
        return best