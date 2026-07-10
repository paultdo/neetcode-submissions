# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()
        curr = root
        if root:
            queue.append(root)
        while queue:
            subArr = []
            currSize = len(queue)
            for i in range(currSize):
                curr = queue[0]
                queue.popleft()
                subArr.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(subArr)
            
        
        return res

        