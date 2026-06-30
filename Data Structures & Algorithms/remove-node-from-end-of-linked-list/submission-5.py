# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            if n == 1 and not head.next:
                return None
            h = head

            l = ListNode(0, head)
            dummy = l
            r = head
            for i in range(n):
                r = r.next
            
            while r:
                r = r.next
                l = l.next
            
            next = l.next.next
            l.next = next

            return dummy.next



            


            

