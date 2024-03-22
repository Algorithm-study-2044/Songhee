# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def search(start, end):
            mid = (start+end)//2
            if isBadVersion(mid):
                if not isBadVersion(mid-1):
                    return mid
                else:
                    return search(start, mid-1)
            else:
                return search(mid+1, end)
        return search(0, n)