# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        head = None
        count = 0

        if not p1:
            return p2
        
        if not p2:
            return p1
        
        if not p1 and not p2:
            return None

        while p1 or p2:
            if p1 and p1.next:
                while p1.next and p1.next.val <= p2.val:
                    if count == 0:
                        head = p1
                    p1 = p1.next
                    count += 1
            if p2 and p2.next:
                while p2.next and p2.next.val < p1.val:
                    if count == 0:
                        head = p2
                    p2 = p2.next
                    count += 1
            if p1 and p2:
                if p1.val <= p2.val:
                    p1_next = p1.next
                    p1.next = p2
                    if count == 0:
                        head = p1
                    p1 = p1_next
                elif p2.val < p1.val:
                    p2_next = p2.next
                    p2.next = p1
                    if count == 0:
                        head = p2
                    p2 = p2_next

                count += 1
            if not p1 or not p2:
                break
        
        return head



            

