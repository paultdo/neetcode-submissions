# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        m = root.val
        return self.helper(root, m)

    def helper(self, root: TreeNode, max: int) -> int:

        curr = 0
        if not root:
            return 0
        if root.val >= max:
            max = root.val
            curr += 1 
        
        left = self.helper(root.left, max)
        right = self.helper(root.right, max)

        return curr + left + right


