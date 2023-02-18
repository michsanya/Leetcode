# Definition for singly-linked list.
from typing import Optional
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListNode(ListNode):
    def __repr__(self):
        return str(self.val) + '->' + str(self.next)

    def add_to_head(self, val):
        node = self
        while node.next != None:
            node = node.next
        node.next = ListNode(val, None)
        return

    def add_to_tail(self, val):
        temp = ListNode(self.val, self.next)
        self.next = temp
        self.val = val
        return


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 2 -> 4 -> 3 add 5 -> 6 -> 4 result 7 -> 0 -> 8
        # 342 + 465 = 807
        result = ListNode()
        adder = 0
        while l1 or l2:
            if l1:
                value_1 = l1.val
            else:
                value_1 = 0
            if l2:
                value_2 = l2.val
            else:
                value_2 = 0
            digit = value_1 + value_2 + adder
            adder = 0
            if digit > 9:
                digit -= 10
                adder = 1
            result.add_to_head(digit)
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        if adder:
            result.add_to_head(adder)

        return result.next


l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
s = Solution()
l3 = s.addTwoNumbers(l1, l2)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val) +'->'+ str(self.next)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 1 -> 2 -> 6 add 2 -> 3 -> 4 result 3 -> 5 -> 0 -> 1
        # 621 + 432 = 1053
        list_of_nodes = []
        adder = 0
        while l1 and l2:
            node = ListNode(l1.val + l2.val + adder, None)
            adder = 0
            if node.val > 9:
                node.val -= 10
                adder = 1
            list_of_nodes.append(node)
            l1 = l1.next
            l2 = l2.next
        if adder > 0:
            list_of_nodes.append(ListNode(adder, None))


        return list_of_nodes


l1 = ListNode(1, ListNode(2, ListNode(6)))
l2 = ListNode(2, ListNode(3, ListNode(4)))

# l1 = ListNode(2, ListNode(4, ListNode(9)))
# l2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9))))

s = Solution()
gg = s.addTwoNumbers(l1, l2)
