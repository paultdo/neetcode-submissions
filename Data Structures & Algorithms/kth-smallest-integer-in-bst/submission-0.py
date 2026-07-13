# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count = 0
    res = -1
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.helper(root, k)
        return self.res
    
    def helper(self, root: TreeNode, k):
        if not root:
            return
        self.helper(root.left, k)
        self.count += 1
        if self.count == k:
            self.res = root.val
        self.helper(root.right, k)