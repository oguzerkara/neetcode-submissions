# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        seen = set()
        dummy = head
        while dummy:

            if dummy.val in seen:
                if dummy.next and dummy.next.val in seen:
                    return True
            seen.add(dummy.val)
            dummy = dummy.next
        return False