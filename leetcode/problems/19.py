# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ans = []
        while True:
            ans.append(head.val)
            next_head = head.next
            if next_head is None:
                break
            head = next_head
        res = None
        index = 0
        while len(ans) > 0:
            index += 1
            a = ans.pop()
            if index == n:
                continue
            res = ListNode(a, res)

        return res
