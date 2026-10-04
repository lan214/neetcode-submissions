"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        copy = {}
        ptr = head
        while ptr:
            new_node = Node(ptr.val)
            copy[ptr] = new_node
            ptr = ptr.next
        
        ptr = head
        while ptr:
            if ptr.next: copy[ptr].next = copy[ptr.next]
            if ptr.random: copy[ptr].random = copy[ptr.random]
            ptr = ptr.next

        return copy[head]