# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        sum_list = dummy
        remainder = 0
        while l1 and l2:
            total = l1.val + l2.val + remainder
            val = total % 10
            sum_list.next = ListNode(val)
            remainder = total // 10
            l1 = l1.next
            l2 = l2.next
            sum_list = sum_list.next

        rest = l1 or l2
        while rest:
            total = rest.val + remainder
            val = total % 10
            sum_list.next = ListNode(val)
            remainder = total // 10
            rest = rest.next
            sum_list = sum_list.next
        
        if remainder:
            sum_list.next = ListNode(1)
        
        return dummy.next