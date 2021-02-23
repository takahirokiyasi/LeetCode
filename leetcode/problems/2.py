class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def addListNode(l1: ListNode, l2: ListNode, add: int) -> ListNode:
            num = (l1.val if l1 else 0) + (l2.val if l2 else 0)
            tem = (num + add) % 10
            nextAdd = (num + add) // 10

            if l1 is None:
                res = ListNode(tem)
                if l2.next is None and nextAdd == 0:
                    res.next = None
                elif l2.next is None:
                    res.next = ListNode(nextAdd)
                else:
                    res.next = addListNode(None, l2.next, nextAdd)
                return res

            if l2 is None:
                res = ListNode(tem)
                if l1.next is None and nextAdd == 0:
                    res.next = None
                elif l1.next is None:
                    res.next = ListNode(nextAdd)
                else:
                    res.next = addListNode(l1.next, None, nextAdd)
                return res

            if l1.next is None and l2.next is None and nextAdd == 0:
                res = ListNode(tem)
                res.next = None
                return res

            if l1.next is None and l2.next is None:
                res = ListNode(tem)
                res.next = ListNode(nextAdd, None)
                return res

            res = ListNode(tem)
            res.next = addListNode(l1.next, l2.next, nextAdd)
            return res

        return addListNode(l1, l2, 0)
