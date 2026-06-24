# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        temp = head

        if not curr:
            return None
        
        if not curr.next:
            return curr
        
        while temp:
            temp = curr.next
            curr.next = prev
            if not temp:
                break
            prev = curr
            curr = temp

        
        return curr
        

