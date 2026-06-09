# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pnt2 = head
        dummy = ListNode(0,head)
        pnt = dummy
        while pnt2:
            if n > 0:
                pnt2 = pnt2.next
                n -= 1
            else:
                pnt2 = pnt2.next
                pnt = pnt.next

        pnt.next = pnt.next.next
        return dummy.next
