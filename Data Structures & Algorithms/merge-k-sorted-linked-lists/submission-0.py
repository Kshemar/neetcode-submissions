# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        op= []
        for i in lists:
            while i:
                op.append(i.val)
                i=i.next
        op.sort()

        res = ListNode(0)
        cur = res

        for j in op:
            cur.next = ListNode(j)
            cur= cur.next
        return res.next