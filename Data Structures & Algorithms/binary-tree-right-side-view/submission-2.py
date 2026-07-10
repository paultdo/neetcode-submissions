# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        res = []
        curr = root
        if curr:
            queue.append(curr)
        
        while queue:
            currSize = len(queue)
            for i in range(currSize):
                curr = queue[0]
                queue.popleft()
                if i == currSize - 1:
                    res.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
            
        
        return res
