# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        half = slow.next
        slow.next = None
        reversed_half = self.reverse(half)
        self.merge(head, reversed_half)

    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def merge(self, l1, l2):
        dummy = ListNode()
        merged = dummy
        while l1 or l2:
            if l1:
                merged.next = l1
                l1 = l1.next
                merged = merged.next
            if l2:
                merged.next = l2
                l2 = l2.next
                merged = merged.next
        return dummy.next

