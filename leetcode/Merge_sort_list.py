# -*- coding: utf-8 -*-
"""
@author: Kaushik Acharya
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    final = ListNode(0)
    curr = final
    print(l1)
    print(l2)
    while l1 and l2:
        print(ListNode(l1.val))
        if l1.val >= ListNode(l2.val):
            curr.next = l2
            l2 = l2.next
        else:
            curr.next = l1
            l1.next = l1.next
        curr = curr.next

    if not l1:
        curr.next = l1
    if not l2:
        curr.next = l2
    # curr.next = l1 or l2
    return final.next




p = mergeTwoLists(mergeTwoLists, [1,2,3], [1,3,4])
print(p)
