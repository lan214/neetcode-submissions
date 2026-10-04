# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for linked_list in lists:
            if linked_list:
                heapq.heappush(min_heap, NodeWrapper(linked_list))
        
        dummy = ListNode()
        current = dummy
        while min_heap:
            wrapper = heapq.heappop(min_heap)
            current.next = wrapper.node
            current = current.next
            if wrapper.node.next:
                heapq.heappush(min_heap, NodeWrapper(wrapper.node.next))

        return dummy.next