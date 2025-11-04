"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        map = {}
        curr = head
        while curr:
            map[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            clone = map[curr]
            clone.next = map.get(curr.next)
            clone.random = map.get(curr.random)
            curr = curr.next
        
        return map[head]
        