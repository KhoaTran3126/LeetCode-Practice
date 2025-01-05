# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        prev = None
        curr = head
        next = None

        while curr!=None:
            ## Moves 'next' pointer forward
            next = curr.next
            ## Reverses linkage; current node points to previous node
            curr.next = prev
            ## Moves position of previous pointer to place of current point
            prev = curr
            ## Moves position of current pointer to place to place of next pointer
            curr = next
        return prev