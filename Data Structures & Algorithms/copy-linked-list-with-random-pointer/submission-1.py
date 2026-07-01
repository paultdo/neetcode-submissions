"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeSet = dict()
        curr = head
        newCurr = Node(-101)

        while curr:
            newCurr.val = curr.val
            nodeSet[curr] = newCurr
            curr = curr.next
            if curr:
                newCurr.next = Node(-101)
                newCurr = newCurr.next
        
        curr = head
        newCurr = next(iter(nodeSet.values()), None)
        while curr and newCurr:
            if curr.random == None:
                newCurr.random = None
            else:
                newCurr.random = nodeSet[curr.random]
            
            curr = curr.next
            newCurr = newCurr.next

        return next(iter(nodeSet.values()), None)



            
