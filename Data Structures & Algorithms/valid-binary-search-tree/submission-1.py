# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, -1000, 1000)


    def helper(self, root: TreeNode, min, max) -> bool:
        if not root:
            return True
        
        if root.val < min:
            return False
        
        if root.val > max:
            return False
        
        return self.helper(root.left, min, root.val - 1) and self.helper(root.right, root.val + 1, max)