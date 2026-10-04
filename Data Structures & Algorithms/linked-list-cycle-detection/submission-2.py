# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if head.next is None:
            return False
        if head.next.next is None:
            return False
        fast = head.next.next
        slow = head.next
        while fast is not None and fast.next is not None and fast != slow:
            fast = fast.next.next
            slow = slow.next
        if fast == slow:
            return True
        else:
            return False