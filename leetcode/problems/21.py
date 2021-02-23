# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def getNextListNode(l1: ListNode, l2: ListNode) -> ListNode:
            if l1 is None and l2 is None:
                return None
            if l1 is None:
                return ListNode(l2.val, getNextListNode(l1, l2.next))
            if l2 is None:
                return ListNode(l1.val, getNextListNode(l1.next, l2))
            if l1.val <= l2.val:
                return ListNode(l1.val, getNextListNode(l1.next, l2))
            else:
                return ListNode(l2.val, getNextListNode(l1, l2.next))

        return getNextListNode(l1, l2)
