# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while True:
            if not slow or not fast:
                return False
            
            slow = slow.next
            fast = fast

            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                break

            if slow == fast:
                return True
        

        return False