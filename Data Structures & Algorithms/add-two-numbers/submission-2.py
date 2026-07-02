# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = l1
        h2 = l2
        newHead = None
        carry = 0
        curr = ListNode(-1)

        while h1 or h2:
            sum = 0
            if h1 and h2:
                sum = h1.val + h2.val + carry
            elif h1 and not h2:
                sum = h1.val + carry
            elif h2 and not h1:
                sum = h2.val + carry
            

            if sum > 9:
                curr.val = (sum % 10)
                carry = sum // 10
            else:
                curr.val = sum
                carry = 0

            if newHead == None:
                newHead = curr
            
            h1 = h1.next if h1 else h1
            h2 = h2.next if h2 else h2
            if h1 or h2:
                curr.next = ListNode(-1)
                curr = curr.next
        
        if carry != 0:
            curr.next = ListNode(carry)

        return newHead