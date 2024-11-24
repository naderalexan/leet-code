from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = None
        while head:
            tmp = head.next
            head.next = cur
            cur = head
            head = tmp
        return cur
