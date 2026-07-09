# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.sameTree(root, subRoot) == True:
            return True
        
        if not root:
            return False
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def sameTree(self, root: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root and not root2:
            return True

        if not root or not root2:
            return False
        
        if root.val != root2.val:
            return False

        return self.sameTree(root.left, root2.left) and self.sameTree(root.right, root2.right)
        