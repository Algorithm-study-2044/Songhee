# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # 33 / 35 testcases passed,
    # trav(x) 방식이 느리다..! 

    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        # def trav(x):
        #     if not x:
        #         return []
        #     return trav(x.left) + [x.val] + trav(x.right)
        
        # def search(x, arr, low, high):
        #     if high < low:
        #         return low
        #     mid = (high+low)//2
        #     if arr[mid] > x:
        #         return search(x, arr, low, mid-1)
        #     elif arr[mid] < x:
        #         return search(x, arr, mid+1, high)
        #     else:
        #         return mid

        def dfs(root: Optional[TreeNode]):
            if root is None:
                return
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)

        arr = []
        dfs(root)
        
        ans = []
        for x in queries:
            i = bisect_left(arr, x + 1) - 1
            j = bisect_left(arr, x)
            mi = arr[i] if 0 <= i < len(arr) else -1
            mx = arr[j] if 0 <= j < len(arr) else -1
            ans.append([mi, mx])
        return ans

        return ans
            