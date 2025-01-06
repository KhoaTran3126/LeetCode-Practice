# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]

        Time Complexity is O(N+M)
        Space Complexity is O(1)
        """
        if list1 is None: return list2
        if list2 is None: return list1

        cur = dummy = ListNode()

        while (list1 is not None) and (list2 is not None):
            if list1.val < list2.val:
                ## Moves 'next' pointer and increases list1's pointer
                cur.next = list1
                list1 = list1.next
            else:
                ## Moves 'next' pointer and increases list2's pointer
                cur.next = list2
                list2 = list2.next
            ## Changees the current pointer to match the position of its 'next'
            cur = cur.next

        ## Pours content of remaining non-empty list into merged list
        if (list1 is not None) or (list2 is not None):
            cur.next = list1 if (list1 is not None) else list2
        return dummy.next


        