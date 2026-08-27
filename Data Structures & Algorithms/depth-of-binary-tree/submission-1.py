# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        s = [(root, 1)]
        res = 0
        while s:
            k,v = s.pop()
            if k:
                res = max(res, v)
                s.append((k.left, v + 1))
                s.append((k.right, v + 1))
        return res