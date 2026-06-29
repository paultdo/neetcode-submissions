# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next

        if size == 0:
            return
        
        curr = head
        curr2 = head
        for i in range(size//2 if size % 2 == 0 else (size//2) + 1):
            curr2 = curr2.next

        curr = head
        curr2 = head
        mid = None
        for i in range(size//2 if size % 2 == 0 else (size//2) + 1):
            mid = curr2
            curr2 = curr2.next

        mid.next = None  # cut the list in half

        # reverse second half

        prev = None
        while curr2:
            temp = curr2.next
            curr2.next = prev
            prev = curr2
            curr2 = temp

        curr2 = prev
        #merge

        while curr2:
            temp1 = curr.next
            temp2 = curr2.next

            curr.next = curr2
            if temp1 and temp1 is not curr2:
                curr2.next = temp1
            curr = temp1
            curr2 = temp2




        


