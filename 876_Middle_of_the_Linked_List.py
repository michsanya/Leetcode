# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head
        list_of_values = []
        while head:
            list_of_values.append(head.val)
            head = head.next

        middle_index = len(list_of_values) // 2
        for i in range(middle_index):
            middle = middle.next
        return middle


ts = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
a = Solution().middleNode(ts)
print(a)

